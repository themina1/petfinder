from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.animal_list),
    url(r'^cats/$', views.cats),
    url(r'^cats/(?P<pk>[0-9]+)/$', views.cats_detail),
    url(r'^cats_adopted_list/$', views.cats_adopted_list),
    url(r'^cats_removed_list/$', views.cats_removed_list),
    url(r'^dogs/$', views.dogs),
    url(r'^dogs/(?P<pk>[0-9]+)/$', views.dogs_detail),
    url(r'^dogs_adopted_list/$', views.dogs_adopted_list),
    url(r'^dogs_removed_list/$', views.dogs_removed_list),
    url(r'^unique/$', views.unique),
    url(r'^unique/(?P<pk>[0-9]+)/$', views.unique_detail),
    url(r'^unique_adopted_list/$', views.unique_adopted_list),
    url(r'^unique_removed_list/$', views.unique_removed_list),
    url(r'^reddit_posts/$', views.reddit_pets)
]

urlpatterns += staticfiles_urlpatterns()