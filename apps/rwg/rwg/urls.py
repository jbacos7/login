from django.conf.urls import url
from . import views
print "love"
urlpatterns = [
    url(r'^$', views.index),
    url(r'^randword', views.randword),
]