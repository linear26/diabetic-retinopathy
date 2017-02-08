import os
import cv2
from shutil import copy
import Image
import exudate
import imutils



import numpy as np
import opticdisk3
import bloodvessel

from imutils import contours
from skimage import measure
import argparse
import imutils



def imlist(path):
    """
    The function imlist returns all the names of the files in 
    the directory path supplied as argument to the function.
    """
    
    return [os.path.join(path, f) for f in os.listdir(path)]
        
        
if __name__=='__main__':
    '''
    This reads all the images in a given folder and returns the results 
    '''

    images_path = imlist("C:/Python27/bag-of-words-master/diaretdb0_fundus_images/jpg_format")
    for image_path in images_path:
        exudate.exudate(image_path)
