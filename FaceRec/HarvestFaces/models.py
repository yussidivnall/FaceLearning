from django.db import models

class RawImage(models.Model):
    image=models.FileField(upload_to='raw');
    person_hints=models.CharField(max_length=512,null=True);
    notes=models.CharField(max_length=512,null=True);
