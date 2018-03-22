from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books),
    url(r'^books/add$', views.booksAdd),
    url(r'^addBook$', views.addBook),
    url(r'^books/(?P<id>\d+)$', views.booksView),
    url(r'^users/(?P<id>\d+)$', views.userProfile),
    url(r'^review$', views.addReview),
    url(r'^delReview/(?P<bookid>\d+)/(?P<id>\d+)$', views.delReview),
]