from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
import json
from marauder.models import *
from marauder.tables import *
from django_tables2 import SingleTableView
from django.http import Http404

# Creature Views
class CreatureListView(SingleTableView):
    model = Creature
    template_name = 'creatures/index.html'
    queryset = Creature.objects.filter(hidden=False)
    table_class = CreatureTable
    table_pagination = {'per_page': 10}

class CreatureDetailView(generic.DetailView):
    model = Creature
    template_name = 'creatures/base.html'

    def get_context_data(self, **kwargs):
        context = super(CreatureDetailView, self).get_context_data(**kwargs)
        if kwargs['object'].hidden:
            raise Http404
        return context

# Character Views
class CharacterListView(SingleTableView):
    model = Character
    template_name = 'characters/index.html'
    queryset = Character.objects.filter(hidden=False)
    table_class = CharacterTable
    table_pagination = {'per_page': 10}

class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = 'characters/base.html'

    def get_context_data(self, **kwargs):
        context = super(CharacterDetailView, self).get_context_data(**kwargs)
        if kwargs['object'].hidden:
            raise Http404
        return context

# Spell Views
class SpellListView(SingleTableView):
    model = Spell
    template_name = 'spells/index.html'
    table_class = SpellTable
    table_pagination = {'per_page': 10}

class SpellDetailView(generic.DetailView):
    model = Spell
    template_name = 'spells/base.html'

# Potion Views
class PotionListView(SingleTableView):
    model = Potion
    template_name = 'potions/index.html'
    queryset = Potion.objects.filter(hidden=False)
    table_class = PotionTable
    table_pagination = {'per_page': 10}

class PotionDetailView(generic.DetailView):
    model = Potion
    template_name = 'potions/base.html'

    def get_context_data(self, **kwargs):
        context = super(PotionDetailView, self).get_context_data(**kwargs)
        if kwargs['object'].hidden:
            raise Http404
        return context

# Story Views
class StoryListView(SingleTableView):
    model = Story
    template_name = 'stories/index.html'
    table_class = StoryTable
    table_pagination = {'per_page': 10}

class StoryDetailView(generic.DetailView):
    model = Story
    template_name = 'stories/base.html'

    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        return context


# Artifact Views
class ArtifactListView(SingleTableView):
    model = Artifact
    template_name = 'artifacts/index.html'
    table_class = ArtifactTable
    table_pagination = {'per_page': 10}

class ArtifactDetailView(generic.DetailView):
    model = Artifact
    template_name = 'artifacts/base.html'

# Book Views
class BookListView(SingleTableView):
    model = Book
    template_name = 'books/index.html'
    table_class = BookTable
    table_pagination = {'per_page': 10}

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/base.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        return context

# Location Views
class LocationListView(SingleTableView):
    model = Location
    template_name = 'locations/index.html'
    #table_class = StoryTable
    #table_pagination = {'per_page': 10}

class LocationDetailView(generic.DetailView):
    model = Location
    template_name = 'locations/base.html'

    def get_context_data(self, **kwargs):
        context = super(LocationDetailView, self).get_context_data(**kwargs)
        return context

# House Views
class HouseListView(generic.ListView):
    model = House
    template_name = 'houses/index.html'

    def get_context_data(self, **kwargs):
        context = super(HouseListView, self).get_context_data(**kwargs)
        return context

class HouseDetailView(generic.DetailView):
    model = House
    template_name = 'creatures/base.html'

    def get_context_data(self, **kwargs):
        context = super(HouseDetailView, self).get_context_data(**kwargs)
        return context

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

        data = formatCharacterData(self, p)

        return JSONResponse(data)

    def formatPotionData(self, p):

        return {
            "id": p.id,
            "title": p.title,
            "difficulty": p.difficulty,
            "physical_description": p.physical_description,
            "effects": p.effects,
            "recipe": p.recipe if p.recipe else None,
            "notable_uses": p.notable_uses
        }

class CreatureRestView(RestView):
    def GET(self, creature_id):
        c = Creature.objects.get(pk=creature_id)

        data = formatCreatureData(self, c)

        return JSONResponse(data)

    def formatCreatureData(self, c):

        return {
            "id": c.id,
            "name": c.name,
            "description": c.description,
            "classification": c.classification,
            "rating": c.rating
        }


class JSONResponse(HttpResponse):
    def __init__(self, data):
        super(JSONResponse, self).__init__(
            content = json.dumps(data, indent=2),
            content_type = "application/json"
        )
