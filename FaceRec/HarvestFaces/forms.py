from django import forms
from multiupload.fields import MultiFileField
from django.forms import formset_factory
class UploadImagesForm(forms.Form):
    tags=forms.CharField(label='tags',widget=forms.Textarea, max_length=512,required=False);
    images=MultiFileField(min_num=1,max_num=20,max_file_size=1024*1024*15,required=False);

class TrainImageForm(forms.Form):
    tags=forms.CharField(max_length=255);
    classifiers=forms.CharField(max_length=255);
    def __init__(self,*args,**kwargs):
        extra = kwargs.pop('extra')
        super(TrainImageForm,self).__init__(*args,**kwargs);
        for i,face in enumerate(extra):
            self.fields["face_%s"%i]=forms.CharField();

