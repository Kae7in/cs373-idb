from django.shortcuts import render
from django.views import generic
from marauder.models import *

# Creature Views
class CreatureListView(generic.ListView):
    model = Creature
    template_name = 'creatures/index.html'

    def get_context_data(self, **kwargs):
        context = super(CreatureListView, self).get_context_data(**kwargs)
        return context

class CreatureDetailView(generic.DetailView):
    model = Creature
    template_name = 'creatures/base.html'

    def get_context_data(self, **kwargs):
        context = super(CreatureDetailView, self).get_context_data(**kwargs)
        return context

# Character Views
class CharacterListView(generic.ListView):
    model = Character
    template_name = 'characters/index.html'

    def get_context_data(self, **kwargs):
        context = super(CharacterListView, self).get_context_data(**kwargs)
        return context

class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = 'characters/base.html'

    def get_context_data(self, **kwargs):
        context = super(CharacterDetailView, self).get_context_data(**kwargs)
        return context

# Spell Views
class SpellDetailView(generic.DetailView):
    model = Spell
    template_name = 'spells/base.html'

# Potion Views
class PotionDetailView(generic.DetailView):
    model = Potion
    template_name = 'potions/base.html'

# Story Views
class StoryDetailView(generic.DetailView):
    model = Story
    template_name = 'stories/base.html'

# Artifact Views
class ArtifactDetailView(generic.DetailView):
    model = Artifact
    template_name = 'artifacts/base.html'

# Book Views
# Location Views
