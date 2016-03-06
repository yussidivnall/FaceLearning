from django.db import models

class RawImage(models.Model):
    image=models.FileField(upload_to='raw');
    tags=models.CharField(max_length=512,null=True);
    harvest_id=models.IntegerField(null=True)
