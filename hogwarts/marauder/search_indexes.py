from haystack import indexes
from marauder.models import *

class CharacterIndex(indexes.SearchIndex, indexes.Indexable):
  # Declare which model attributes are included in indexing/searching
  text = indexes.CharField(document=True, use_template=True) # This is the index document Haystack will build for searching
  name = indexes.CharField(model_attr='name')
  wand = indexes.CharField(model_attr='wand')
  description = indexes.CharField(model_attr='description')

  def get_model(self):
      return Character

  def index_queryset(self, using=None):
      """
      Used when the entire index for model is updated. You can filter out things
      that don't need refiltering?
      """
      return self.get_model().objects


class CreatureIndex(indexes.SearchIndex, indexes.Indexable):
  # Declare which model attributes are included in indexing/searching
  text = indexes.CharField(document=True, use_template=True) # This is the index document Haystack will build for searching
  name = indexes.CharField(model_attr='name')
  description = indexes.CharField(model_attr='description')

  def get_model(self):
      return Creature

  def index_queryset(self, using=None):
      """
      Used when the entire index for model is updated. You can filter out things
      that don't need refiltering?
      """
      return self.get_model().objects

class LocationIndex(indexes.SearchIndex, indexes.Indexable):
  # Declare which model attributes are included in indexing/searching
  text = indexes.CharField(document=True, use_template=True) # This is the index document Haystack will build for searching
  name = indexes.CharField(model_attr='name')
  kind = indexes.CharField(model_attr='kind')
  description = indexes.CharField(model_attr='description')

  def get_model(self):
      return Location

  def index_queryset(self, using=None):
      """
      Used when the entire index for model is updated. You can filter out things
      that don't need refiltering?
      """
      return self.get_model().objects

class PotionIndex(indexes.SearchIndex, indexes.Indexable):
  # Declare which model attributes are included in indexing/searching
  text = indexes.CharField(document=True, use_template=True) # This is the index document Haystack will build for searching
  name = indexes.CharField(model_attr='title')
  effects = indexes.CharField(model_attr='effects')
  recipe = indexes.CharField(model_attr='recipe')
  description = indexes.CharField(model_attr='effects')

  def get_model(self):
      return Potion

  def index_queryset(self, using=None):
      """
      Used when the entire index for model is updated. You can filter out things
      that don't need refiltering?
      """
      return self.get_model().objects

class BookIndex(indexes.SearchIndex, indexes.Indexable):
  # Declare which model attributes are included in indexing/searching
  text = indexes.CharField(document=True, use_template=True) # This is the index document Haystack will build for searching
  name = indexes.CharField(model_attr='name')

  def get_model(self):
      return Book

  def index_queryset(self, using=None):
      """
      Used when the entire index for model is updated. You can filter out things
      that don't need refiltering?
      """
      return self.get_model().objects

class ArtifactIndex(indexes.SearchIndex, indexes.Indexable):
   text = indexes.CharField(document=True, use_template=True)
   name = indexes.CharField(model_attr='name')
   description = indexes.CharField(model_attr='description')
   kind = indexes.CharField(model_attr='kind')

   def get_model(self):
       return Artifact

   def index_queryset(self, using=None):
       return self.get_model().objects


class SpellIndex(indexes.SearchIndex, indexes.Indexable):
   text = indexes.CharField(document=True, use_template=True)
   name = indexes.CharField(model_attr='incantation')
   description = indexes.CharField(model_attr='effect')

   def get_model(self):
       return Spell

   def index_queryset(self, using=None):
       return self.get_model().objects
