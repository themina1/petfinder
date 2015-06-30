from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.animal_list),
    url(r'^cats/$', views.cats),
    url(r'^cats/(?P<pk>[0-9]+)/$', views.cats_detail),
    url(r'^dogs/$', views.dogs),
    url(r'^dogs/(?P<pk>[0-9]+)/$', views.dogs_detail),
    url(r'^unique/$', views.unique),
    url(r'^unique/(?P<pk>[0-9]+)/$', views.unique_detail),
]

urlpatterns += staticfiles_urlpatterns()