from django.db import models
from FaceRec.models import Person;
from PIL import Image
import pdb
class RawImage(models.Model):
    image=models.FileField(upload_to='raw/');
    harvest_id=models.CharField(default=-1,max_length=512);
    def __str__(self):
        return str(self.image)
    
    #TODO make this work and resize
    #use pillow somehow
    def save(self, *args, **kwargs):
            if not self.image or not self.harvest_id:
                print("Missing stuff for image"+self.image)
                return;
            super(RawImage,self).save()
            img=Image.open(self.image)
            img=img.resize( (300,300) , Image.ANTIALIAS)
            img.save(self.image.path)
            print(self.image.path)
            #pdb.set_trace()
            

class RawFace(models.Model):
    image=models.FileField(upload_to='raw');
    src=models.ManyToManyField(RawImage);
    person=models.ForeignKey(Person,null=True);
    x=models.IntegerField(default=0)
    y=models.IntegerField(default=0)
    width=models.IntegerField(default=0)
    height=models.IntegerField(default=0)
    def __str__(self):
        return str(image)
