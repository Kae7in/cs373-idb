from django.conf.urls import patterns, url

from library import views as lib_views

urlpatterns = patterns('',
	#/
    url(r'^$', lib_views.index, name='index'),

    #Characters
    #/characters/
    url(r'^characters/$', lib_views.characters, name='characters'),
    #/characters/5/
    url(r'^characters/(?P<character_id>\d+)/$', lib_views.character, name='character'),

    #Spells
    #/spells/
    url(r'^spells/$', lib_views.spells, name='spells'),
    #/spells/5/
    url(r'^spells/(?P<spell_id>\d+)/$', lib_views.spell, name='spell'),

    #Potions
    #/potions/
    url(r'^potions/$', lib_views.potions, name='potions'),
    #/potions/5/
    url(r'^potions/(?P<potion_id>\d+)/$', lib_views.potion, name='potion'),
    #/potions/5/brew/
    url(r'^potions/(?P<potion_id>\d+)/brew/$', lib_views.brew, name='brew'),

    #Creatures
    #/creatures/
    url(r'^creatures/$', lib_views.creatures, name='creatures'),
    #/creatures/5/
    url(r'^creatures/(?P<creature_id>\d+)/$', lib_views.creature, name='creature'),
    #/creatures/5/neutralize/
    url(r'^creatures/(?P<creature_id>\d+)/neutralize/$', lib_views.neutralize, name='neutralize'),

    #Locations
    #/locations/
    url(r'^locations/$', lib_views.locations, name='locations'),
    #/locations/5/
    url(r'^locations/(?P<location_id>\d+)/$', lib_views.location, name='location'),

    #Artifacts
    #/artifacts/
    url(r'^artifacts/$', lib_views.artifacts, name='artifacts'),
    #/artifacts/5/
    url(r'^artifacts/(?P<artifact_id>\d+)/$', lib_views.artifact, name='artifact'),

    #Books
    #/books/
    url(r'^books/$', lib_views.books, name='books'),
    #/books/5/
    url(r'^books/(?P<book_id>\d+)/$', lib_views.book, name='book'),

    #Stories
    #/stories/
    url(r'^stories/$', lib_views.stories, name='stories'),
    #/stories/5/
    url(r'^stories/(?P<story_id>\d+)/$', lib_views.story, name='story'),
)