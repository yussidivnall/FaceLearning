from django.conf.urls import patterns, include, url
from django.conf import settings
#from imdb_training.views import *
from .views import *
urlpatterns = [
    url(r'^$',start_page),
    url(r'^upload$',UploadImagesView.as_view()),
    url(r'^uploading$',uploading_images_page),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
