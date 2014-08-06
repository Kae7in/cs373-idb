from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from marauder import views
from django.conf import settings
from django.conf.urls.static import static
from haystack.forms import SearchForm

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name='index.html')),
    (r'^base.html$', TemplateView.as_view(template_name='base.html')),
    (r'^splash.html$', TemplateView.as_view(template_name='splash.html')),
    (r'^about/$', TemplateView.as_view(template_name='about.html')),
    (r'^citations/$', TemplateView.as_view(template_name='citations.html')),

    #Creatures
    url(r'^creatures/$', views.CreatureListView.as_view(), name='creatures'),
    url(r'^creatures/(?P<pk>\d+)/$', views.CreatureDetailView.as_view(), name='creature'),
    #Characters
    url(r'^characters/$', views.CharacterListView.as_view(), name='characters'),
    url(r'^characters/(?P<pk>\d+)/$', views.CharacterDetailView.as_view(), name='character'),
    #Potions
    url(r'^potions/$', views.PotionListView.as_view(), name='potions'),
    url(r'^potions/(?P<pk>\d+)/$', views.PotionDetailView.as_view(), name='potion'),
    #Artifacts
    url(r'^artifacts/$', views.ArtifactListView.as_view(), name='artifacts'),
    url(r'^artifacts/(?P<pk>\d+)/$', views.ArtifactDetailView.as_view(), name='artifact'),
#    url(r'^artifacts/$', views.ArtifactListView.as_view(), name='artifacts'),
    #Spells
    url(r'^spells/$', views.SpellListView.as_view(), name='spells'),
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
    url(r'^shops/(?P<pk>\d+)/$', views.ShopDetailView.as_view(), name='shop'),
    url(r'^schools/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='school'),
    #Houses
    url(r'^houses/$', views.HouseListView.as_view(), name='houses'),
    url(r'^houses/(?P<pk>\d+)/$', views.HouseDetailView.as_view(), name='house'),

    #############
    #### API ####
    #############
    url(r'^api/characters/$', views.CharacterRestView(), name='characters_api'),
    url(r'^api/characters/(?P<id>\d+)/$', views.CharacterRestView(), name='character_api'),

    url(r'^api/stories/$', views.StoryRestView(), name='stories_api'),
    url(r'^api/stories/(?P<id>\d+)/$', views.StoryRestView(), name='story_api'),

    url(r'^api/spells/$', views.SpellRestView(), name='spells_api'),
    url(r'^api/spells/(?P<id>\d+)/$', views.SpellRestView(), name='spell_api'),

    url(r'^api/shops/$', views.ShopRestView(), name='shops_api'),
    url(r'^api/shops/(?P<id>\d+)/$', views.ShopRestView(), name='shop_api'),

    url(r'^api/potions/$', views.PotionRestView(), name='potions_api'),
    url(r'^api/potions/(?P<id>\d+)/$', views.PotionRestView(), name='potion_api'),

    url(r'^api/creatures/$', views.CreatureRestView(), name='creatures_api'),
    url(r'^api/creatures/(?P<id>\d+)/$', views.CreatureRestView(), name='creature_api'),

    url(r'^api/artifacts/$', views.ArtifactRestView(), name='artifacts_api'),
    url(r'^api/artifacts/(?P<id>\d+)/$', views.ArtifactRestView(), name='artifact_api'),

    url(r'^api/schools/$', views.SchoolRestView(), name='schools_api'),
    url(r'^api/schools/(?P<id>\d+)/$', views.SchoolRestView(), name='school_api'),

    ################
    #### SEARCH ####
    ################
    url(r'^search/', views.MySearchView(my_form_class=SearchForm), name='haystack_search'),

    ####################
    #### OTHER API #####
    ####################
    url(r'^experience/$', views.otherapi, name='experience'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
