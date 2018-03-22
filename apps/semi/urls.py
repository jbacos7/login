from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users),
    url(r'^users/new$', views.new),
    url(r'^users/(?P<number>\d)$', views.show),
    url(r'^users/(?P<number>\d)/edit$', views.edit),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<number>\d)/destroy', views.destroy)
]