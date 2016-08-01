#!/usr/bin/python3
import cv2
from cv2 import *
import pdb
import sys,os

class extract_faces(object):

    # Returns squares matching a classifier
    # returns [ [x y w h],[....] ]  #squares of positions of faces in image
    @staticmethod
    def get_squares(image_path,classifier_path):
        print(image_path)
        image=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        if image is None:
            print("No image loaded : "+image_path)
            return None
        classifier=cv2.CascadeClassifier(classifier_path) #TODO check this is valid
        faces = classifier.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = 0
        )
        return faces #TODO check everything worked, maybe raise an exception if not.


"""
if __name__=='__main__':
    images_dir='/home/volcan/Development/OpenCV/FaceLearning3/FaceRec/raw/'
    cascade_dir='/home/volcan/Development/OpenCV/FaceLearning3/FaceRec/classifiers/'

    squares=extract_faces.get_squares(images_dir+"P50517-191652_UcxPJRb.jpg",cascade_dir+"haarcascade_frontalface_default.xml")
    print(squares)
"""
