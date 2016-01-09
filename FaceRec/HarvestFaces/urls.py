from django.conf.urls import patterns, include, url
from django.conf import settings
#from imdb_training.views import *
from .views import *
urlpatterns = [
    url(r'^$',start_page),
    url(r'^imdb$',imdb_start_page),
    url(r'^imdb/results$',imdb_start_page),


    url(r'^google$',imdb_start_page),
    url(r'^uploading$',uploading_images_page),
    url(r'^upload$',upload_images_page),
    url(r'^upload_image$',upload_image_page),
    url(r'^video$',imdb_start_page),
]

if settings.DEBUG:
    urlpatterns += url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': '/home/volcan/Development/OpenCV/FaceLearning/media','show_indexes':True}),
