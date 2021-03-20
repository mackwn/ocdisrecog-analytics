import cv2  
import numpy as np
import pandas as pd
import os
import pickle

def load_header_df():
    return pd.read_csv('data/full_df.csv')

def img_to_vector(fn, resize=None, imgdir='data/preprocessed_images'):
    '''
    Take input filename for preprocessed fundus image.
    Assumes resolution of 512 px by 512 px. 
    Returns a 1 dimensional row vector

    Input - file name of 512x512 preprocessed image data
    imgdir - directory of preprocessed image data
    resize - None or tuple of integer dimensions (list like of len 2)
    '''
    #print(imgdir, fn)
    path = os.path.join(imgdir, fn)

    img = cv2.imread(path)

    if img is None: raise ValueError('Unable to open image file, Check the filename and directory')

    if resize is not None:
        #img = cv2.resize(img, resize)
        try:
            img = cv2.resize(img, resize)
        except:
            raise TypeError('Unable to resize, Ensure resize is a valid tuple of dimensions')
        try:
            img = img.reshape(1, resize[0]*resize[1]*3)
        except: 
            raise ValueError('Unable to reshpae resized image.')
    else:
        try:
            img = img.reshape(1, 512*512*3)
        except:
            raise ValueError('Unable to reshape image. Ensure the image is 512 px by 512 px')

    return img

def header_to_img_matrix(df, resize=None, imgdir='data/preprocessed_images', save=None):
    '''
    Convert dataframe of image header data and converts into numpy array. 
    Inputs -  dataframe, directory of images, and optionaal reshape dimensions
    Outputs - numpy array of header data and numpy array of image data
    '''

    # Extract data from dataframe
    data = df.values
    data_cols = list(df.columns.values)
    # Make sure filename is passed
    if 'filename' not in data_cols: raise ValueError('Dataframe must contain a filename column.')
    
    # Iterate over each row of data an extract an image for each filename
    img_features = None
    for row in data:
        fn = row[-1]
        #print(fn)
        img = img_to_vector(fn, resize, imgdir)
        if img_features is None: img_features=img
        else: img_features=np.concatenate((img_features, img))

    img_features = np.array(img_features) 

    if save is not None:
        pickle.dump((data, img_features), open("data/{}.pkl".format(save), "wb"))


    return data, img_features
