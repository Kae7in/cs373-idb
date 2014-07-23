from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
import json
from marauder.models import *

class IndexView(generic.ListView):
    template_name = 'index.html'

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
        # Pull the character row from the model. TODO
        c = Character.objects.get(pk=character_id) 

        # Manipulate the python dict into the appropriate form
        data = {
            "id": c.id, 
            "name": c.name, 
            "wand": c.wand if c.wand else None,
            "description": c.description,
            "magical": c.magical,
            "quote": c.quote if c.quote else None,
            "quote_by": c.quote_by if c.quote_by else None 
        }
        
        # Form the python dict into a JSON HTTP response 
        return JSONResponse(data)

class PotionRestView(RestView):

    def GET(self, potion_id):
    p = Potion.objects.get(pk=potion_id)

    data = {
        "id": p.id,
        "name": p.title,
        "difficulty": p.difficulty,
        "effects": p.effects,
        "physical description": p.physical_description,        
        "recipe": p.recipe if p.recipe else None,
        "notable uses": p.notable_uses
    }
    return JSONResponse(data)
         
        

class JSONResponse(HttpResponse):
    def __init__(self, data):
        super(JSONResponse, self).__init__(
            content = json.dumps(data, indent=2),
            content_type = "application/json"
        )
