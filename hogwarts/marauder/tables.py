import django_tables2 as tables
from marauder.models import *

class CharacterTable(tables.Table):
    name = tables.TemplateColumn('''
    	<a href='{% url "character" record.pk %}'>{{ record.name }}</a>''')
    class Meta:
        model = Character
        fields = ("name", "magical", "sex", "creature", "school_attended", "house")
        attrs = {"class": "table table-striped table-bordered table-hover"}

class StoryTable(tables.Table):
    date = tables.TemplateColumn("{{ record.formatted_date }}")
    name = tables.TemplateColumn('''
    	<a href='{% url "story" record.pk %}'>{{ record.name }}</a>''')
    kind = tables.TemplateColumn("{{ record.kind|capfirst }}")

    class Meta:
        model = Story
        fields = ("name", "kind", "date")
        attrs = {"class": "table table-striped table-bordered table-hover"}

class CreatureTable(tables.Table):
    name = tables.TemplateColumn('''
    	<a href='{% url "creature" record.pk %}'>{{ record.name }}</a>''')
    classification = tables.TemplateColumn("{{ record.classification }}")
    rating = tables.TemplateColumn("{{ record.get_rating_display }}")
    class Meta:
        model = Creature
        fields = ("name", "classification", "rating")
        attrs = {"class": "table table-striped table-bordered table-hover"}