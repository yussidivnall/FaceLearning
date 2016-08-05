from django.conf.urls import patterns, include, url
from django.conf import settings
#from imdb_training.views import *
from .views import *
from django.contrib.staticfiles import views


#TODO remove views.serve in production!!!
urlpatterns = [
    url(r'^$',start_page),
    url(r'^upload$',UploadImagesView.as_view()),
    url(r'^train$', FaceLabelingView.as_view()),
    url(r'^static/(?P<path>.*)$',views.serve),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#JIC
#    url(r'^train$',HarvestTrainingView.as_view()),
