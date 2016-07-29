from django.db import models
from FaceRec.models import Person;
class RawImage(models.Model):
    image=models.FileField(upload_to='raw');
    tags=models.CharField(max_length=512,null=True);
    harvest_id=models.CharField(default=-1,max_length=512);

class RawFace(models.Model):
    image=models.FileField(upload_to='raw');
    src=models.ManyToManyField(RawImage);
    person=models.ForeignKey(Person,null=True);
    x=models.IntegerField(default=0)
    y=models.IntegerField(default=0)
    width=models.IntegerField(default=0)
    height=models.IntegerField(default=0)
