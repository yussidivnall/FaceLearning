from django import forms
from multiupload.fields import MultiFileField
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet

#dataset for classifier, something like /celebrities/actors/
#this form is to save an X by Y image of face, and store it in 
#/media/dataset/celebrities/actors/label-N.jpg
#where N is a unique per face index 
class FaceForm(forms.Form):
    dataset=forms.CharField(max_length=255) 
    label=forms.CharField(max_length=255)    

class BaseFacesFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        for form in self.forms:
            if form.cleaned_data:
               label=form.cleaned_data['label']
               dataset=form.cleaned_data['dataset']

