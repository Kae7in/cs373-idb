from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from marauder import views

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name='index.html')),
    (r'^base.html$', TemplateView.as_view(template_name='base.html')),
    (r'^splash.html$', TemplateView.as_view(template_name='splash.html')),
    url(r'^creatures/(?P<pk>\d+)/$', views.CreatureView.as_view(), name='creatures'),
    url(r'^characters/(?P<pk>\d+)/$', views.CharacterView.as_view(), name='characters'),
    url(r'^potions/(?P<pk>\d+)/$', views.PotionsView.as_view(), name='potions'),
    url(r'^artifacts/(?P<pk>\d+)/$', views.ArtifactsView.as_view(), name='artifacts'),
    url(r'^spells/(?P<pk>\d+)/$', views.SpellsView.as_view(), name='spells'),
    url(r'^stories/(?P<pk>\d+)/$', views.StoriesView.as_view(), name='stories'),

    # API
    url(r'^api/characters/(?P<id>\d+)/$', views.CharacterRestView())
    url(r'^api/potions/(?P<id>\d+)/$', views.PotionRestView())
    url(r'^api/creatures/(?P<id>\d+)/$', views.CreatureRestView())
)
