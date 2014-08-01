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


class PotionIndex(indexes.SearchIndex, indexes.Indexable):
  # Declare which model attributes are included in indexing/searching
  text = indexes.CharField(document=True, use_template=True) # This is the index document Haystack will build for searching
  title = indexes.CharField(model_attr='title')
  effects = indexes.CharField(model_attr='effects')
  recipe = indexes.CharField(model_attr='recipe')

  def get_model(self):
      return Potion

  def index_queryset(self, using=None):
      """
      Used when the entire index for model is updated. You can filter out things
      that don't need refiltering?
      """
      return self.get_model().objects
