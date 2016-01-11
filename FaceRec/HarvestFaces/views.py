from django.shortcuts import render

from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
#from django.core.context_processors import csrf
from django.template import RequestContext
from django import forms
from .forms import *
from .models import *
from django.views.generic.edit import FormView
#import imdb_utils
#import face_utils
def start_page(request):
    return render_to_response('HarvestFaces/start_page.html')
# Create your views here.

def uploading_images_page(request):
    return render_to_response('HarvestFaces/imdb/start_page.html')

class UploadImagesView(FormView):
    template_name='HarvestFaces/upload_images.html';
    form_class=UploadImagesForm;
    success_url='uploading'
    def form_valid(self,form):
        for img in form.cleaned_data['images']:
            hints=form.cleaned_data['person_hints']
            notes=form.cleaned_data['notes']
            RawImage.objects.create(image=img,person_hints=hints,notes=notes)
#            RawImage.objects.create(image=img,notes=notes)
        return super(UploadImagesView,self).form_valid(form)
