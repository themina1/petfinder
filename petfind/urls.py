from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^cats/$', views.cats),
    url(r'^dogs/$', views.dogs),
    url(r'^unique/$', views.unique),
]