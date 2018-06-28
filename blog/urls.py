from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^animal/cat_list/$', views.cat_list, name='cat_list'),
    url(r'^animal/dog_list/$', views.dog_list, name='dog_list'),
    url(r'^animal/(?P<pk>\d+)/$', views.animal_detail, name='animal_detail'),
    url(r'^animal/(?P<pk>\d+)/edit/$', views.animal_edit, name='animal_edit'),
    url(r'^animal/(?P<pk>\d+)/remove/$', views.animal_remove, name='animal_remove'),
    url(r'^animal/new/$', views.animal_new, name='animal_new'),
    url(r'^animal/(?P<pk>\d+)/animove/$', views.animal_animove, name='animal_animove'),
    url(r'^drafts/$', views.draft_list, name='draft_list'),
]