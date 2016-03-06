from django import forms
from multiupload.fields import MultiFileField
class UploadImagesForm(forms.Form):
    tags=forms.CharField(label='tags',widget=forms.Textarea, max_length=512,required=False);
    images=MultiFileField(min_num=1,max_num=20,max_file_size=1024*1024*15,required=False);
