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
