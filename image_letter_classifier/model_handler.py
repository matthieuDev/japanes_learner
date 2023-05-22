

import csv
import numpy as np
import tensorflow as tf

from handle_image_file import clean_image


def load_model(load_file='model.h5'):
    return tf.keras.models.load_model(load_file)

def load_categories(categories_file='data/k49_classmap.csv'):
    with open(categories_file, encoding='utf8') as f :
        csv_characters = csv.reader(f, delimiter=',')
        next(csv_characters)
        return np.array([symbol for _, _, symbol in csv_characters])
    
class model_handler :
    def __init__ (self, load_file='model.h5', categories_file='data/k49_classmap.csv', size_img = 28):
        self.model = load_model(load_file)
        self.categories = load_categories(categories_file)
        self.size_img = size_img

    def predict(self, img):
        print('iiiiiiiiiiimg', img.shape)
        img = clean_image(img, self.size_img)
        img = img[np.newaxis, :, :, np.newaxis]
        prediction = self.model.predict(img)
        return self.categories[prediction.argmax()]