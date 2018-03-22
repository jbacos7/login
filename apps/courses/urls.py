from django.conf.urls import url
from . import views
print "*"*100
urlpatterns = [
    url(r'^$', views.index),
    url(r'^destroy/(?P<number>\d+)$', views.destroy),
    url(r'^destroy/(?P<number>\d+)/confirm$', views.confirm),
    url(r'^process$', views.process),
]



