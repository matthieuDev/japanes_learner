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

def get_start_stop_true (arr_ok) :
    '''
    get the position of the first and last true element from 1-d bool array
    '''
    good_start, good_end = 0,0
    start_stop = False
    for i, is_ok in enumerate(arr_ok):
        if is_ok :
            if not start_stop :
                good_start = i
                start_stop = True
            good_end = i
        
    return good_start, good_end + 1

def clean_image(img):
    '''
    
    '''
    size_clean = 28
    clean_image = np.zeros((size_clean, size_clean), dtype=int)
    
    if (clean_image.shape == img.shape) :
        return img
    
    #delete lines and columns that are empty
    line_ok = (img > 20).any(axis=1)
    column_ok = (img > 20).any(axis=0)

    start_line, end_line = get_start_stop_true (line_ok)
    start_column, end_column = get_start_stop_true (column_ok)

    img = img[start_line: end_line, start_column: end_column]

    i_step = img.shape[0] / size_clean
    j_step = img.shape[1] / size_clean

    for i_clean, i_img in enumerate(np.arange(0, img.shape[0], i_step)) :
        for j_clean, j_img in enumerate(np.arange(0, img.shape[1], j_step)) :
            clean_image[i_clean, j_clean] = np.mean(img[round(i_img): round(i_img + i_step), round(j_img): round(j_img + j_step)], dtype=int)
            '''clean_image[i_clean, j_clean] = (
                np.mean(img[round(i_img): round(i_img + i_step), round(j_img): round(j_img + j_step)], dtype=int)
            ) / (i_step * j_step)'''
          
    return clean_image

def print_img (img_arr):
    plt.imshow(img_arr)
