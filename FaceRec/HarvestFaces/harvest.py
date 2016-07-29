import cv2
from cv2 import *;
import numpy;
from glob import glob
from django.conf import settings

class Faces:
    classifiers_path=""
    def __init__(self,c_path=""):
        print("Init");
        if c_path=="": c_path=settings.CLASSIFIERS_PATH
        self.classifiers_path=c_path
        self.populate_classifiers();
        #print(settings.CLASSIFIERS_PATH);

    def populate_classifiers(self):
        self.classifiers=[];
        for classifier_path in glob(self.classifiers_path+"*.xml"):
            classifier=cv2.CascadeClassifier(classifier_path);
            self.classifiers.append(classifier)

    def get_classifiers(self):
        return self.classifiers;

    #returns squares where cascade found faces
    def find_faces(self,image,cascade):
        #Todo finetune this, see
        #http://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html#cascadeclassifier-detectmultiscale

        ret=cascade.detectMultiScale(image);
        if(len(ret)==0):return None 
        else: return ret 
    
    def get_all_faces(self,image):
        ret=[]
        for c in self.get_classifiers():
            for f in faces.find_faces(image,c):
                ret.append(f);
        ret,weight=cv2.groupRectangles(ret,1,1)
        #print("weight: "+str(weight));
        return ret;
            
    
#To test
if __name__=='__main__':
    classifiers_path="/home/volcan/Development/OpenCV/FaceLearning3/FaceRec/classifies/"
    test_image="/home/volcan/tmp/people1.jpg"
    faces=Faces(classifiers_path);
    #image=cv2.LoadImage("/home/volcan/tmp/people1.jpg",cv.CV_LOAD_IMAGE_COLOR)
    image=cv2.imread(test_image,cv2.IMREAD_COLOR);
    test=faces.get_all_faces(image);
    print(test)
