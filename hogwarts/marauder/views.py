from django.shortcuts import render
from django.views import generic
from marauder.models import *
from django.db.models import get_app, get_models
from django.template import RequestContext, loader
from django.http import HttpResponse

def index(request):
    model_items = {}
    app = get_app('marauder')
    for model in get_models(app):
        model_items[model.__name__] = model.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {'model_items': model_items})
    return HttpResponse(template.render(context))

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
