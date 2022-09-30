import json
import os

from werkzeug.datastructures import FileStorage

def test_home_page(test_client):
    """
    GIVEN a Flask application configured
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Create a test client using the Flask application configured for testing
    response = test_client.get('/')
    assert response.status_code == 200


def test_predict_api(test_client):
    """
    GIVEN I am at Predict page
    WHEN I Upload An Image to /Predict (POST)
    THEN I get predictions of the image
    """
    # Create a test client using the Flask application configured for testing
    print(os.getcwd())
    upload_file = "test/feature/resource/test_image.jpeg"

    file = FileStorage(
        stream=open(upload_file, "rb"),
        filename="test_image_predict.jpeg",
    ),
    content_type = 'multipart/form-data'
    data = {'file': file}
    response = test_client.post('/Predict', content_type=content_type, data=data)
    assert response.status_code == 200

    json_response = dict(json.loads(response.get_data(as_text=True)))
    assert 'result' in json_response
    result = json_response['result']
    assert isinstance(result, (list, float))


def test_upload_unlabelled_image_api(test_client):
    """
    GIVEN I am at Predict page
    WHEN I Upload An Image to /unlabelled-images (POST)
    THEN I get predictions of the image
    """
    # Create a test client using the Flask application configured for testing

    upload_file = "test/feature/resource/test_image.jpeg"

    file = FileStorage(
        stream=open(upload_file, "rb"),
        filename="test_image_unlabelled.jpeg",
    ),
    content_type = 'multipart/form-data'
    data = {'file': [file]}
    response = test_client.post('/unlabelled-images', content_type=content_type, data=data)
    assert response.status_code == 200

    json_response = dict(json.loads(response.get_data(as_text=True)))
    assert 'status' in json_response
    status = json_response['status']
    assert status == 'success'


def test_get_unlabelled_images_pagination_api(test_client):
    """
    WHEN I set a GET request to /unlabelled-images
    THEN I should get paging information of the labelled images
    """

    # Create a test client using the Flask application configured for testing
    response = test_client.get('/unlabelled-images')
    json_response = json.loads(response.get_data(as_text=True))
    assert 'filenames' in json_response
    filenames = json_response['filenames']
    assert response.status_code == 200
    assert isinstance(filenames, list)


def test_get_labelled_images_pagination_api(test_client):
    """
    WHEN I set a GET request to /labelled-images
    THEN I should get paging information of the labelled images
    """

    # Create a test client using the Flask application configured for testing
    response = test_client.get('/labelled-images')
    json_response = json.loads(response.get_data(as_text=True))
    assert 'filenames' in json_response
    filenames = json_response['filenames']
    assert response.status_code == 200
    assert isinstance(filenames, list)


def test_get_single_image_api(test_client):
    """
    WHEN I send a get request to /images/<image name>
    THEN I should get a binary image
    """
    # Create a test client using the Flask application configured for testing
    response = test_client.get('/images/test_image_unlabelled.jpeg')
    assert response.status_code == 200
    assert 'image' in response.content_type
    assert response.get_data() is not None


def test_change_images_label_api(test_client):
    """
    GIVEN I am at labelled images page
    WHEN I change the image label to good
    THEN The returned response should be success
    """

    # Create a test client using the Flask application configured for testing
    data = {'label': 'good'}
    response = test_client.put('/images/sample_image.jpeg', json=data)
    assert response.status_code == 200
    json_response = json.loads(response.get_data(as_text=True))
    assert 'status' in json_response
    status = json_response['status']
    assert status == 'success'
