from django.db import models

class Person(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    profile_picture=models.ImageField(null=True);

#Label should be "Person.first_name Person.last_name Person.pk" to ensure uniqueness
#If person or label not speficied, assume not classified.
class Face(models.Model):
    image=models.ImageField();
    person=models.ForeignKey(Person,null=True); 
    label=models.CharField(null=True);

