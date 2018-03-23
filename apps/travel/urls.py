from django.conf.urls import url
from . import views

app_name = 'exam'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^travels$', views.travels, name='travels'),
    url(r'^travels/destination/(?P<trip_id>\d+)$', views.destination, name='destination'),
    url(r'^travels/add$', views.addtravel, name='addtravel'),
    url(r'^checktravel$', views.checktravel, name='checktravel'),
    url(r'^checkuser$', views.checkuser, name='checkuser'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^jointravel/(?P<trip_id>\d+)$', views.jointravel, name='jointravel'),
]