from django.conf.urls import patterns, url
from marauder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<topic>\w+)/(?P<creature_id>\d+)/$', views.creature_detail, name='creature_detail'),    
)
