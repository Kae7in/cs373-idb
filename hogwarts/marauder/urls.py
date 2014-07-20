from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from marauder import views

urlpatterns = patterns('',
    url(r'^creatures/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)
