from django import forms
from multiupload.fields import MultiFileField
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet
class UploadImagesForm(forms.Form):
    images=MultiFileField(min_num=1,max_num=20,max_file_size=1024*1024*15,required=False);

class FaceForm(forms.Form):
    raw=forms.CharField(max_length=255) #raw image (300x300) path in ../media/raw
    dataset=forms.CharField(max_length=255) #some dataset eg. /celebrities/actors/
    label=forms.CharField(max_length=255) #A label for face.
    x=forms.IntegerField()
    y=forms.IntegerField()
    width=forms.IntegerField()
    height=forms.IntegerField()

class BaseFaceFormSet(BaseFormSet):
    def clean(self):
       if any(self.errors):return
       if self.cleaned_data:
            dataset=self.cleaned_data['dataset'] 
            label=self.cleaned_data['label'] 
            x=self.cleaned_data['x'] 
            y=self.cleaned_data['y'] 
            width=self.cleaned_data['width'] 
            height=self.cleaned_data['height'] 
