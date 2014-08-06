import django_tables2 as tables
from marauder.models import *

class CharacterTable(tables.Table):
    name = tables.TemplateColumn('''
    	<a href='{% url "character" record.pk %}'>{{ record.name }}</a>''')
    creature = tables.TemplateColumn('''
        {% if record.creature and not record.creature.hidden %}
            <a href='{% url "creature" record.creature.id %}'>
        {% endif %}
        {{ record.creature.name }}
        {% if record.creature and not record.creature.hidden %}
            </a>
        {% endif %}''')
    school_attended = tables.TemplateColumn('''
        {% if record.school_attended %}
            <a href='{% url "school" record.school_attended.id %}'>
                {{ record.school_attended.name }}
            </a>
        {% endif %}''')
    house = tables.TemplateColumn('''
        {% if record.house %}
            <a href='{% url "house" record.house.id %}'>
                {{ record.house.name }}
            </a>
        {% endif %}''')
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
    classification = tables.TemplateColumn("{{ record.get_classification_display }}")
    rating = tables.TemplateColumn("{{ record.get_rating_display }}")
    class Meta:
        model = Creature
        fields = ("name", "classification", "rating")
        attrs = {"class": "table table-striped table-bordered table-hover"}

class BookTable(tables.Table):
    name = tables.TemplateColumn('''
        <a href='{% url "book" record.pk %}'>{{ record.name }}</a>''')
    author = tables.TemplateColumn('''
        {% if record.author and not record.author.hidden %}
            <a href='{% url "character" record.author.id %}'>
        {% endif %}
        {{ record.author.name }}
        {% if not record.author.hidden %}
            </a>
        {% endif %}''')

    class Meta:
        model = Book
        fields = ("name", "author")
        attrs = {"class": "table table-striped table-bordered table-hover"}

class PotionTable(tables.Table):
    title = tables.TemplateColumn('''
        <a href='{% url "potion" record.pk %}'>{{ record.title }}</a>''')
    difficulty = tables.TemplateColumn("{{ record.get_difficulty_display }}")

    class Meta:
        model = Potion
        fields = ("title", "difficulty")
        attrs = {"class": "table table-striped table-bordered table-hover"}

class ArtifactTable(tables.Table):
    name = tables.TemplateColumn('''
        <a href='{% url "artifact" record.pk %}'>{{ record.name }}</a>''')
    kind = tables.TemplateColumn("{{ record.kind|capfirst }}")

    class Meta:
        model = Artifact
        fields = ("name", "kind")
        attrs = {"class": "table table-striped table-bordered table-hover"}

class SpellTable(tables.Table):
    incantation = tables.TemplateColumn('''
        <a href='{% url "spell" record.pk %}'>{{ record.incantation }}</a>''')
    kind = tables.TemplateColumn("{{ record.kind }}")
    difficulty = tables.TemplateColumn("{{ record.get_difficulty_display }}")
    unforgivable = tables.TemplateColumn("{% if record.unforgivable %}<center><img src='{{ STATIC_URL }}images/skull_glyphicon.png'/></center>{% endif %}")

    class Meta:
        model = Spell
        fields = ("incantation", "alias", "creator", "unforgivable", "difficulty", "kind")
        attrs = {"class": "table table-striped table-bordered table-hover"}

class LocationTable(tables.Table):
    name = tables.TemplateColumn('''
        <a href='{% url "location" record.pk %}'>{{ record.name }}</a>''')
    kind = tables.TemplateColumn("{{ record.kind|capfirst }}")

    class Meta:
        model = Location
        fields = ("name", "kind")
        attrs = {"class": "table table-striped table-bordered table-hover"}
