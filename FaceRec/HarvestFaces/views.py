from django.shortcuts import render

from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
#from django.core.context_processors import csrf
from django.template import RequestContext
from django import forms
from .forms import *
#import imdb_utils
#import face_utils
def start_page(request):
    return render_to_response('HarvestFaces/start_page.html')
# Create your views here.

def imdb_start_page(request):
    return render_to_response('HarvestFaces/imdb/start_page.html')

def upload_image_page(request):
    if request.method=="POST":
        print("POST")
        form = upload_image_form(request.POST,request.FILES)
        if form.is_valid():
            print("is_valid");
            return HttpResponseRedirect("uploading");
        else: print ("Form invalid");
    else:
        print("GET");
        form = upload_image_form()
    return render(request,'HarvestFaces/upload_image.html',{'form':form})        

def upload_images_page(request):
    if request.method=="POST":
        form = upload_images_form(request.POST,request.FILES)
        if form.is_valid():
            print("Valid form");
            #print (len(form.cleaned_data['images']));
            return HttpResponseRedirect("uploading");
        else:
            print("Invalid form");
    else:
        form = upload_images_form()
    return render(request,'HarvestFaces/upload_images.html',{'form':form})        
#    return render_to_response('HarvestFaces/upload_images.html')

def uploading_images_page(request):
    return render_to_response('HarvestFaces/imdb/start_page.html')
