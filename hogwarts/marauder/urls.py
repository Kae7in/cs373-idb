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
    url(r'^potions/$', views.CharacterListView.as_view(), name='potions'),
    url(r'^potions/(?P<pk>\d+)/$', views.PotionDetailView.as_view(), name='potion'),
    #Artifacts
    url(r'^artifacts/$', views.CharacterListView.as_view(), name='artifacts'),
    url(r'^artifacts/(?P<pk>\d+)/$', views.ArtifactDetailView.as_view(), name='artifact'),
    #Spells
    url(r'^spells/$', views.CharacterListView.as_view(), name='spells'),
    url(r'^spells/(?P<pk>\d+)/$', views.SpellDetailView.as_view(), name='spell'),
    #Stories
    url(r'^stories/$', views.StoryListView.as_view(), name='stories'),
    url(r'^stories/(?P<pk>\d+)/$', views.StoryDetailView.as_view(), name='story'),
    #Books
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book'),
    #Locations
    url(r'^locations/$', views.LocationListView.as_view(), name='locations'),
    url(r'^locations/(?P<pk>\d+)/$', views.LocationDetailView.as_view(), name='location'),
    #Houses
    url(r'^houses/$', views.HouseListView.as_view(), name='houses'),
    url(r'^houses/(?P<pk>\d+)/$', views.HouseDetailView.as_view(), name='house'),

    # API
    url(r'^api/characters/(?P<id>\d+)/$', views.CharacterRestView()),
    url(r'^api/potions/(?P<id>\d+)/$', views.PotionRestView()),
    url(r'^api/creatures/(?P<id>\d+)/$', views.CreatureRestView())

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
