from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from marauder import views

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name='index.html')),
    (r'^base.html$', TemplateView.as_view(template_name='base.html')),
    (r'^splash.html$', TemplateView.as_view(template_name='splash.html')),

    #Creatures
    url(r'^creatures/$', views.CreatureListView.as_view(), name='creatures'),
    url(r'^creatures/(?P<pk>\d+)/$', views.CreatureDetailView.as_view(), name='creature'),
    #Characters
#    url(r'^characters/$', views.CharacterListView.as_view(), name='characters'),
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
)
