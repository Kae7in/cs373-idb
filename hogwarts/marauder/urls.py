from django.conf.urls import patterns, url
from django.views.generic import TemplateView
import marauder.views as mar_views

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', TemplateView.as_view(template_name='index.html')),
    (r'^base.html$', TemplateView.as_view(template_name='base.html')),
    (r'^splash.html$', TemplateView.as_view(template_name='splash.html')),
    #Characters
    (r'^characters/$', TemplateView.as_view(template_name='characters/index.html')),
    (r'^characters/1$', TemplateView.as_view(template_name='characters/1.html')),
    (r'^characters/2$', TemplateView.as_view(template_name='characters/2.html')),
    (r'^characters/3$', TemplateView.as_view(template_name='characters/3.html')),
    (r'^characters/4$', TemplateView.as_view(template_name='characters/4.html')),
    (r'^characters/5$', TemplateView.as_view(template_name='characters/5.html')),
    (r'^characters/6$', TemplateView.as_view(template_name='characters/6.html')),
    #Potions
    (r'^potions/$', TemplateView.as_view(template_name='potions/index.html')),
    (r'^potions/1$', TemplateView.as_view(template_name='potions/1.html')),
    (r'^potions/2$', TemplateView.as_view(template_name='potions/2.html')),
    (r'^potions/3$', TemplateView.as_view(template_name='potions/3.html')),
    #Spells
    (r'^spells/$', TemplateView.as_view(template_name='spells/index.html')),
    (r'^spells/1$', TemplateView.as_view(template_name='spells/1.html')),
    (r'^spells/2$', TemplateView.as_view(template_name='spells/2.html')),
    (r'^spells/3$', TemplateView.as_view(template_name='spells/3.html')),
    #Creatures
    (r'^creatures/$', TemplateView.as_view(template_name='creatures/index.html')),
    (r'^creatures/1$', TemplateView.as_view(template_name='creatures/1.html')),
    (r'^creatures/2$', TemplateView.as_view(template_name='creatures/2.html')),
    (r'^creatures/3$', TemplateView.as_view(template_name='creatures/3.html')),
    #Artifacts
    (r'^artifacts/$', TemplateView.as_view(template_name='artifacts/index.html')),
    (r'^artifacts/1$', TemplateView.as_view(template_name='artifacts/1.html')),
    (r'^artifacts/2$', TemplateView.as_view(template_name='artifacts/2.html')),
    (r'^artifacts/3$', TemplateView.as_view(template_name='artifacts/3.html')),
    #Shops
    (r'^shops/$', TemplateView.as_view(template_name='shops/index.html')),
    (r'^shops/1$', TemplateView.as_view(template_name='shops/1.html')),
    (r'^shops/2$', TemplateView.as_view(template_name='shops/2.html')),
    (r'^shops/3$', TemplateView.as_view(template_name='shops/3.html')),
    #Stories
    (r'^stories/$', TemplateView.as_view(template_name='stories/index.html')),
    (r'^stories/1$', TemplateView.as_view(template_name='stories/1.html')),
    (r'^stories/2$', TemplateView.as_view(template_name='stories/2.html')),
    (r'^stories/3$', TemplateView.as_view(template_name='stories/3.html')),
)
