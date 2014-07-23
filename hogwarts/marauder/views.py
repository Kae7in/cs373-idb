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
    which delegates to model-specific subclasses.
  """

  # Dispatch to the proper child method implementation
  def __call__(self, request, *args, **kwargs):
      allowed_methods = ('GET') # Currently our API only services GET
      if not request.method in allowed_methods:
          response = HttpResponse("Method Not Allowed: %s" % request.method)
          response.status_code = 405
          return response

      if 'id' in kwargs:
          return getattr(self, 'get_item')(kwargs['id'])
      else:
          return getattr(self, 'get_collection')()


class CharacterRestView(RestView):

    def get_item(self, character_id):
        # Pull the character row from the model. 
        c = Character.objects.get(pk=character_id) 

        # Manipulate the python dict to conform to our API 
        data = self.formatCharacterData(c)
        
        # Form the python dict into a JSON HTTP response 
        return JSONResponse(data)

    def get_collection(self):
        # Pull the character row from the model. 
        characters = Character.objects.all()

        # Manipulate the python dict to conform to our API 
        data = []
        for character in characters:
            element = self.formatCharacterData(character)
            data.append(element) 
        
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

class SpellRestView(RestView):
    def get_item(self, spell_id):
        # get the spell from the model
        s = Spell.objects.get(pk=spell_id)

        # fetch data in acceptable format for api
        data = self.formatSpellData(s)

        # return JSON HTTP response
        return JSONResponse(data)

    def get_collection(self):
        # get all spells from the model
        spells = Spell.objects.all()

        # fetch data in acceptable format for api
        data = []
        for spell in spells:
            element = self.formatSpellData(spell)
            data.append(element)

        # return JSON HTTP response
        return JSONResponse(data)

    def formatSpellData(self, s):
        return {
            "id": s.id,
            "incantation": s.incantation,
            "alias": s.alias,
            "effect": s.effect,
            "creator": s.creator,
            "notable_uses": s.notable_uses,
            "unforgivable": s.unforgivable,
            "KIND_CHOICES": s.KIND_CHOICES,
            "DIFFICULTY_CHOICES": s.DIFFICULTY_CHOICES,
            "difficulty": s.difficulty,
            "kind": s.kind,
            "image": s.image,
            "creature": s.creature if s.creature else None
        }


class ShopRestView(RestView):
    def get_item(self, spell_id):
        # get the shop from the model
        s = Shop.objects.get(pk=shop_id)

        # fetch data in acceptable format for api
        data = self.formatShopData(s)

        # return JSON HTTP response
        return JSONResponse(data)

    def get_collection(self):
        # get all shop from the model
        shop = Shop.objects.all()

        # fetch data in acceptable format for api
        data = []
        for spell in shop:
            element = self.formatShopData(spell)
            data.append(element)

        # return JSON HTTP response
        return JSONResponse(data)

    def formatShopData(self, s):
        return {
            "id": s.id,
            "locations": s.locations if s.locations else None
        }

class JSONResponse(HttpResponse):
    def __init__(self, data):
        super(JSONResponse, self).__init__(
            content = json.dumps(data, indent=2),
            content_type = "application/json"
        )
