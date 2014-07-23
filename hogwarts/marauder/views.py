from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
import json
from marauder.models import *
from marauder.tables import *
from django_tables2 import SingleTableView

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
class CharacterListView(SingleTableView):
    model = Character
    template_name = 'characters/index.html'
    table_class = CharacterTable
    table_pagination = {'per_page': 10}

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
"""
  RESTful API
  
  A helpful example at: https://djangosnippets.org/snippets/1740/ 
"""

class RestView(object):
  """
    Serves API GET requests with a JSON response. This is the base class
    which delgates to model-specific subclasses.
  """

  # Dispatch to the proper child method implementation
  def __call__(self, request, *args, **kwargs):
      allowed_methods = ('GET') # Currently our API only services GET
      if not request.method in allowed_methods:
          response = HttpResponse("Method Not Allowed: %s" % request.method)
          response.status_code = 405
          return response

      return getattr(self, request.method)(kwargs['id'])

class CharacterRestView(RestView):

    def GET(self, character_id):
        # Pull the character row from the model. 
        c = Character.objects.get(pk=character_id) 

        # Manipulate the python dict to conform to our API 
        data = self.formatCharacterData(c)
        
        # Form the python dict into a JSON HTTP response 
        return JSONResponse(data)

    def formatCharacterData(self, c):
        """
        Form the given character object into a dictionary that meets API
        specification.
        """
        return {
            "id": c.id, 
            "name": c.name, 
            "wand": c.wand if c.wand else None,
            "description": c.description,
            "magical": c.magical,
            "quote": c.quote if c.quote else None,
            "quote_by": c.quote_by if c.quote_by else None
        }

class PotionRestView(RestView):

    def GET(self, potion_id):
        p = Potion.objects.get(pk=potion_id)

        data = {
            "id": p.id,
            "title": p.title,
            "difficulty": p.difficulty,
            "physical_description": p.physical_description,        
            "effects": p.effects,
            "recipe": p.recipe if p.recipe else None,
            "notable_uses": p.notable_uses
        }
        return JSONResponse(data)
         
class CreatureRestView(RestView):
    def GET(self, creature_id):
        c = Creature.objects.get(pk=creature_id)

        data = {
            "id": c.id,
            "name": c.name,
            "description": c.description,
            "classification": c.classification,
            "rating": c.rating
        }

        return JSONResponse(data)
        

class JSONResponse(HttpResponse):
    def __init__(self, data):
        super(JSONResponse, self).__init__(
            content = json.dumps(data, indent=2),
            content_type = "application/json"
        )