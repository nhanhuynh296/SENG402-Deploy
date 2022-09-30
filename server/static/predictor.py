import os

import numpy as np
import tensorflow as tf
import logging


def image_size_from_filename(filename):
    if 'VGG16' in filename or 'EfficientnetB4' in filename:
        return 224, 224, 3
    elif 'model' in filename:
        return 512, 512, 3


class Predictor():
    def __init__(self, model_dir):
        logging.basicConfig(level=logging.INFO)
        self.model_name = os.path.join(model_dir, 'static', 'VGG16_golden_binary.h5')
        self.model = tf.keras.models.load_model(self.model_name, compile=False)

    def predict(self, image_path):
        img_PIL = tf.keras.preprocessing.image.load_img(image_path,
                                                        target_size=image_size_from_filename(self.model_name))

        img_array = tf.keras.preprocessing.image.img_to_array(img_PIL)
        img_array = tf.expand_dims(img_array, 0)  # Create batch size axis
        predictions = self.model.predict(img_array, verbose=False)
        predictions = predictions[0].astype(np.float64)

        if self.model_name.__contains__("categorical"):
            good = predictions[1]
            bad = predictions[0]
            logging.info(f"This image is {100 * good:.2f} percent good and {100 * bad:.2f} percent bad.")
            return predictions.tolist()
        if self.model_name.__contains__("binary"):
            score = 1 - predictions[0]
        else:
            score = predictions[0]
        logging.info(f"This image is {100 * (1 - score):.2f} percent bad and {100 * score:.2f} percent good.")
        return score
