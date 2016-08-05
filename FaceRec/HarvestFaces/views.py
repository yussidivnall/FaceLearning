from django.shortcuts import render,redirect,get_object_or_404
from extra_views import FormSetView


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
import pdb;
from .extract_faces import extract_faces




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
        #pdb.set_trace()
        session_id=self.harvest_id();
        print("Session ID: "+session_id+"\n");
        for img in form.cleaned_data['images']:
            # Resize image, set as jpeg and store
            RawImage.objects.create(image=img,harvest_id=session_id);
            
        return super(UploadImagesView,self).form_valid(form)







class FaceLabelingView(FormSetView):
    template_name = 'HarvestFaces/faces_formset.html'
    classifier="classifiers/haarcascade_frontalface_default.xml"
    form_class = FaceForm
    success_url = 'success/'
    default_dataset='people/'

    def get_initial(self):
        # return whatever you'd normally use as the initial data for your formset.
      return data

    def formset_valid(self, formset):
        # do stuff
        return super(MyFormSetView, self).formset_valid(formset)

    
    def get(self,request):
        sid=request.session['harvest_id'];
        images=RawImage.objects.filter(harvest_id=sid)
        context={'images':[]}
        
        for img in images:
            forms=[]
            squares=extract_faces.get_squares(str(img),self.classifier)
            for sqr in squares:
                form = FaceForm( 
                    initial={'x':sqr[0],'y':sqr[1],'width':sqr[2],'height':sqr[3],'dataset':self.default_dataset}
                )
                forms.append(form);
                pdb.set_trace()
            faces=zip(forms,squares)
            entry={'src':str(img) , 'faces':faces}
            context['images'].append(entry)
        return render(request,self.template_name,context);


class HarvestTrainingView(FormView):
    template_name='HarvestFaces/train.html';
    classifier="classifiers/haarcascade_frontalface_default.xml"

    def get(self,request):
        sid=request.session['harvest_id'];
        images=RawImage.objects.filter(harvest_id=sid)
        context={'images':[]}
        for img in images:
            #squares=extract_faces.extract_faces().get_squares(self.classifier,str(img))
            squares=extract_faces.get_squares(str(img),self.classifier)
            print("Squares: \n"+str(squares) )
            entry={'src':str(img) , 'squares':squares}
            context['images'].append(entry)
        #pdb.set_trace()
        return render(request,self.template_name,context);
    
