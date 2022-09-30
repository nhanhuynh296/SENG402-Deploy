import os
from flask import Flask, jsonify, request, send_file, abort, Response
from flask_cors import CORS, cross_origin
import pandas as pd
from static import Predictor
from helper import PaginationDataFrameIterator

SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_SAVE_TARGET = 'images'


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.config['DEBUG'] = True
    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    print('loaded COR')
    return app


def init() -> [Predictor, PaginationDataFrameIterator]:
    try:
        df = pd.read_feather(os.path.join(IMAGES_SAVE_TARGET, 'label-data.feather'))
        print("Database loaded")
    except FileNotFoundError:
        df = pd.DataFrame({'filename': pd.Series(dtype='str'),
                           'label': pd.Series(dtype='int64')})

    os.makedirs(os.path.join('src/backend/temp'), exist_ok=True)
    os.makedirs(os.path.join(IMAGES_SAVE_TARGET), exist_ok=True)
    _predictor = Predictor(model_dir=os.path.join(SERVER_DIR))
    _images_iterator = PaginationDataFrameIterator(dataframe=df, save_location=os.path.join(IMAGES_SAVE_TARGET))
    return _predictor, _images_iterator


app: Flask = create_app()
predictor, images_iterator = init()
images_iterator.sync_folder()


# sanity check route
@app.route('/', methods=['GET'])
def home():
    return jsonify('Backend connected :) !')


@app.route('/Predict', methods=['POST'])
def upload_and_predict_image():
    file = request.files['file']
    filename = file.filename
    file_path = os.path.join('src/backend/temp', filename)

    file.save(file_path)
    print('save to', file_path)
    prediction = predictor.predict(file_path)
    response_object = {'status': 'success', 'result': prediction}
    return jsonify(response_object)


@app.route('/Upload', methods=['GET', 'POST'])
def upload_images():
    abort(404)


@app.route('/unlabelled-images', methods=['GET', 'POST'])
def unlabelled_images_upload_and_pagination():
    if request.method == 'GET':
        page_length = int(request.args.get('page_length', default=5))
        page = int(request.args.get('page', default=1))
        images_filename = images_iterator.get_top_unlabelled_filename(page=page, page_length=page_length)
        response = {'page_length': page_length, 'filenames': images_filename}
        return jsonify(response)
    elif request.method == 'POST':
        files = request.files.getlist('file')

        filenames = []
        for file in files:
            filename = file.filename
            filenames.append(filename)
            file_path = os.path.join(IMAGES_SAVE_TARGET, filename)
            file.save(file_path)
            print('save to', file_path)
        images_iterator.add_image(image_filename=filenames)
        return jsonify({'status': 'success'})


@app.route('/labelled-images', methods=['GET'])
def get_labelled_pagination():
    # todo add support for uploading pre annotated images
    page_length = int(request.args.get('page_length', default=5))
    page = int(request.args.get('page', default=1))
    total_pages = images_iterator.get_pagination_of_type(type_of="labelled", page_length=page_length)
    images_filename = images_iterator.get_labelled_paginated(page=page, page_length=page_length)
    response = {'total_pages': total_pages, 'page_length': page_length, 'filenames': images_filename}
    return jsonify(response)


@app.route('/images/<image_filename>', methods=['GET'])
def get_images(image_filename):
    filename = os.path.join(IMAGES_SAVE_TARGET, image_filename)
    if not os.path.isfile(filename):
        abort(404)

    if request.method == 'GET':
        _, file_extension = os.path.splitext(filename)
        return send_file(os.path.abspath(filename), mimetype=f'image/{file_extension[1:]}')


@app.route('/images/<image_filename>', methods=['PUT'])
def change_image_label(image_filename):
    post_data = request.get_json()
    label = str(post_data.get('label', None)).lower()
    if label is None:
        abort(Response("No label found in body"))
    if label not in ["good", "bad", "marginal"]:
        abort(Response('Label must either be "good" or "bad" or "marginal"', 401))

    images_iterator.change_label(image_filename, str(post_data['label']).lower())
    images_iterator.save_df()
    return jsonify(status='success')
