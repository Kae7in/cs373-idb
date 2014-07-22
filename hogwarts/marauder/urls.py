from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from marauder import views

urlpatterns = patterns('',
    url(r'^$', , name='index'),
    #Creatures
    url(r'^creatures/$', views.CreatureListView.as_view(), name='creatures'),
    url(r'^creatures/(?P<pk>\d+)/$', views.CreatureDetailView.as_view(), name='creature'),
    #Characters
    url(r'^characters/$', views.CharacterListView.as_view(), name='characters'),
    url(r'^characters/(?P<pk>\d+)/$', views.CharacterDetailView.as_view(), name='character'),
    #Potions
    url(r'^potions/(?P<pk>\d+)/$', views.PotionDetailView.as_view(), name='potion'),
    #Artifacts
    url(r'^artifacts/(?P<pk>\d+)/$', views.ArtifactDetailView.as_view(), name='artifact'),
    #Spells
    url(r'^spells/(?P<pk>\d+)/$', views.SpellDetailView.as_view(), name='spell'),
    #Stories
    url(r'^stories/(?P<pk>\d+)/$', views.StoryDetailView.as_view(), name='story'),

)
