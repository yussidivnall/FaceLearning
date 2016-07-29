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
#from uuid import uuid4;
import uuid

from .harvest import Faces

#import imdb_utils
#import face_utils
def start_page(request):
    return render_to_response('HarvestFaces/start_page.html')
# Create your views here.



#
# view of the upload/ page and keep a session cookie 
#
class UploadImagesView(FormView):
    template_name='HarvestFaces/upload_images.html';
    form_class=UploadImagesForm;
    success_url='train'


    def harvest_id(self):
        print(type(self.request.session));
        session_id=str(uuid.uuid4());
        self.request.session['harvest_id']=session_id;
        return session_id;

    def form_valid(self,form):
        session_id=self.harvest_id();
        print("Session ID: "+session_id+"\n");
        for img in form.cleaned_data['images']:
            tags=form.cleaned_data['tags'];
            RawImage.objects.create(image=img,tags=tags,harvest_id=session_id);
            
        return super(UploadImagesView,self).form_valid(form)






class HarvestTrainingView(FormView):
    template_name='HarvestFaces/train.html';
    def get(self,request):
        sid=request.session['harvest_id'];
        print("SID %s"%sid)
        images=RawImage(harvest_id=sid);
        print(type(images))
        faces=Faces();
        classifiers=faces.get_classifiers();
        t_args=[];
        print(type(images))
        print("Harvest ID"+images.harvest_id)
        return render(request,'HarvestFaces/train.html');
    
