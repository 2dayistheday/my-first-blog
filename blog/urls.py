from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name ='main'),
    url(r'^group/$', views.group, name ='group'),
    url(r'^drive/$', views.drive, name ='drive'),
    url(r'^post/$', views.post_list, name ='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^content/getusermedia/gum/$', views.gum, name='gum'),
    url(r'^content/getusermedia/canvas/$', views.canvas, name='canvas'),
    url(r'^content/getusermedia/resolution/$', views.resolution, name='resolution'),
    url(r'^content/peerconnection/pc1/$', views.pc1, name='pc1'),
]
