from django.conf.urls import patterns, url

import library.views as lib_views

urlpatterns = ('',
    (r'^$', 'direct_to_template', {'template': 'index.html'}),
    #Characters
    (r'^characters/1$', 'direct_to_template', {'template': 'characters/1.html'}),
    (r'^characters/2$', 'direct_to_template', {'template': 'characters/2.html'}),
    (r'^characters/3$', 'direct_to_template', {'template': 'characters/3.html'}),
    #Potions
    (r'^potions/1$', 'direct_to_template', {'template': 'potions/1.html'}),
    (r'^potions/2$', 'direct_to_template', {'template': 'potions/2.html'}),
    (r'^potions/3$', 'direct_to_template', {'template': 'potions/3.html'}),
    #Spells
    (r'^spells/1$', 'direct_to_template', {'template': 'spells/1.html'}),
    (r'^spells/2$', 'direct_to_template', {'template': 'spells/2.html'}),
    (r'^spells/3$', 'direct_to_template', {'template': 'spells/3.html'}),
    #Creatures
    (r'^creatures/1$', 'direct_to_template', {'template': 'creatures/1.html'}),
    (r'^creatures/2$', 'direct_to_template', {'template': 'creatures/2.html'}),
    (r'^creatures/3$', 'direct_to_template', {'template': 'creatures/3.html'}),       
    #Artifacts
    (r'^artifacts/1$', 'direct_to_template', {'template': 'artifacts/1.html'}),
    (r'^artifacts/2$', 'direct_to_template', {'template': 'artifacts/2.html'}),
    (r'^artifacts/3$', 'direct_to_template', {'template': 'artifacts/3.html'}),
    #Locations
    (r'^locations/1$', 'direct_to_template', {'template': 'locations/1.html'}),
    (r'^locations/2$', 'direct_to_template', {'template': 'locations/2.html'}),
    (r'^locations/3$', 'direct_to_template', {'template': 'locations/3.html'}),
)