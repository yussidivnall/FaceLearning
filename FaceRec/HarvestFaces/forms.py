from django import forms
from multiupload.fields import MultiFileField

class upload_images_form(forms.Form):
    person_hints=forms.CharField(label='Person hints' ,max_length=512,required=False);
    notes=forms.CharField(label='notes',widget=forms.Textarea, max_length=512,required=False);
    images=MultiFileField(min_num=1,max_num=20,max_file_size=1024*1024*15,required=False);

class upload_image_form(forms.Form):
    person_hints=forms.CharField(label='Person hints' ,max_length=512,required=False);
    notes=forms.CharField(label='Notes', max_length=512,widget=forms.Textarea,required=False);
    image=forms.FileField(required=True);
