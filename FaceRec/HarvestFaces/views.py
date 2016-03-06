from django.shortcuts import render,redirect,get_object_or_404


from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
#from django.core.context_processors import csrf
from django.template import RequestContext
from django import forms
from .forms import *
from .models import *
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from uuid import uuid4;

#import imdb_utils
#import face_utils
def start_page(request):
    return render_to_response('HarvestFaces/start_page.html')
# Create your views here.

class UploadImagesView(FormView):
    template_name='HarvestFaces/upload_images.html';
    form_class=UploadImagesForm;
    success_url='train'


    def harvest_id(self):
        print(type(self.request.session));
        self.request.session['harvest_id']=str(uuid4());

    def form_valid(self,form):
        self.harvest_id();
        for img in form.cleaned_data['images']:
            tags=form.cleaned_data['tags'];
            RawImage.objects.create(image=img,tags=tags);
            
        return super(UploadImagesView,self).form_valid(form)

class HarvestTrainingView(FormView):
    template_name='HarvestFaces/train.html';
    def get(self,request):
        sid=request.session['harvest_id'];
        print(sid);
        return HttpResponse("Training...");

