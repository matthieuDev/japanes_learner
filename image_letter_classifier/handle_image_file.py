import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from math import floor , ceil

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
    clean_image = np.zeros((size_clean, size_clean), dtype=float)
    
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
        i_img_ceil = ceil(i_img)
        i_img_up_decimal_number = i_img_ceil - i_img

        i_next_img = i_img + i_step
        next_i_img_floor = floor(i_next_img)
        next_i_img_decimal_number = i_next_img - next_i_img_floor
        for j_clean, j_img in enumerate(np.arange(0, img.shape[1], j_step)) :            
            j_img_ceil = ceil(j_img)
            j_img_up_decimal_number = j_img_ceil - j_img

            j_next_img = j_img + j_step
            next_j_img_floor = floor(j_next_img)
            next_j_img_decimal_number = j_next_img - next_j_img_floor
            
            clean_image[i_clean, j_clean] = (
                np.sum(img[i_img_ceil: next_i_img_floor, j_img_ceil: next_j_img_floor], dtype=int) +
                
                np.sum(img[floor(i_img), j_img_ceil: next_j_img_floor]) * i_img_up_decimal_number +
                np.sum(img[i_img_ceil: next_i_img_floor, floor(j_img)]) * j_img_up_decimal_number +

                img[floor(i_img), floor(j_img)] * i_img_up_decimal_number * j_img_up_decimal_number 
            )
            
            if next_i_img_decimal_number :
                clean_image[i_clean, j_clean] += (
                    np.sum(img[next_i_img_floor, j_img_ceil: next_j_img_floor]) * next_i_img_decimal_number +
                    img[next_i_img_floor, floor(j_img)] * next_i_img_decimal_number * j_img_up_decimal_number
                )
            
            if next_j_img_decimal_number :
                clean_image[i_clean, j_clean] += (
                    np.sum(img[i_img_ceil: next_i_img_floor, next_j_img_floor]) * next_j_img_decimal_number +
                    img[floor(i_img), next_j_img_floor] * i_img_up_decimal_number * next_j_img_decimal_number
                )
                if next_i_img_decimal_number :
                    clean_image[i_clean, j_clean] +=\
                        img[next_i_img_floor, next_j_img_floor] * next_i_img_decimal_number * next_j_img_decimal_number
            
    clean_image = np.round(clean_image / (i_step * j_step))

    return clean_image

def print_img (img_arr):
    plt.imshow(img_arr)
