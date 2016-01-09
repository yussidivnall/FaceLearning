from django.shortcuts import render

from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
#from django.core.context_processors import csrf
from django.template import RequestContext
from django import forms
def start_page(request):
    return render_to_response('start_page.html')
