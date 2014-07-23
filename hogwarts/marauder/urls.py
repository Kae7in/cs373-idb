from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from marauder import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name='index.html')),
    (r'^base.html$', TemplateView.as_view(template_name='base.html')),
    (r'^splash.html$', TemplateView.as_view(template_name='splash.html')),

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

    # API
    url(r'^api/characters/(?P<id>\d+)/$', views.CharacterRestView()),
    url(r'^api/potions/(?P<id>\d+)/$', views.PotionRestView()),
    url(r'^api/creatures/(?P<id>\d+)/$', views.CreatureRestView())

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
