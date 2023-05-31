

import csv, os, numpy as np
import tensorflow as tf

from .handle_image_file import clean_image

file_path = os.path.dirname(__file__) + '/'

def load_model(load_file='model.h5'):
    return tf.keras.models.load_model(load_file)

def load_categories(categories_file='data/k49_classmap.csv'):
    with open(categories_file, encoding='utf8') as f :
        csv_characters = csv.reader(f, delimiter=',')
        next(csv_characters)
        return np.array([symbol for _, _, symbol in csv_characters])
    
class model_handler :
    def __init__ (self, load_file= file_path+'model.h5', categories_file= file_path+'data/k49_classmap.csv', size_img = 28):
        self.model = load_model(load_file)
        self.categories = load_categories(categories_file)
        self.size_img = size_img

    def predict(self, img):
        img = clean_image(img, self.size_img)
        img = img[np.newaxis, :, :, np.newaxis] / 255
        prediction = self.model.predict(img)
        return self.categories[prediction.argmax()]