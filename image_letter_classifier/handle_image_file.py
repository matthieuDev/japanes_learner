import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def load_image(image_file, has_white_background = True) :
    '''
    The training set is white on black. If the given image is black on white, use has_white_background to switch the white and black
    '''
    img=mpimg.imread(image_file)
    img = img.mean(axis=2, dtype=int)
    if has_white_background:
        img = 255 - img
    
    return img

def clean_image(img):
    size_clean = 28
    clean_image = np.zeros((size_clean, size_clean), dtype=int)
    
    if (clean_image.shape == img.shape) :
        return img

    i_step = img.shape[0] / size_clean
    j_step = img.shape[1] / size_clean

    for i_clean, i_img in enumerate(np.arange(0, img.shape[0], i_step)) :
        for j_clean, j_img in enumerate(np.arange(0, img.shape[1], j_step)) :
            clean_image[i_clean, j_clean] = np.mean(img[round(i_img): round(i_img + i_step), round(j_img): round(j_img + j_step)], dtype=int)
          
    return clean_image

def print_img (img_arr):
    plt.imshow(img_arr)
