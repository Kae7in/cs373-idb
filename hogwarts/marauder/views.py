from django.shortcuts import render
from django.views import generic
from marauder.models import *

class CreatureView(generic.DetailView):
    model = Creature
    template_name = 'creatures/base.html'

class CharacterView(generic.DetailView):
    model = Character
    template_name = 'characters/base.html'

class SpellsView(generic.DetailView):
    model = Spell
    template_name = 'spells/base.html'

class PotionsView(generic.DetailView):
    model = Potion
    template_name = 'potions/base.html'

class StoriesView(generic.DetailView):
    model = Story
    template_name = 'stories/base.html'

class ArtifactsView(generic.DetailView):
    model = Artifact
    template_name = 'artifacts/base.html'
