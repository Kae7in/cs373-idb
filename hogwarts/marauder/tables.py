import django_tables2 as tables
from marauder.models import *

class CharacterTable(tables.Table):
    name = tables.TemplateColumn('''
    	<a href='{% url "character" record.pk %}'>{{ record.name }}</a>''')
    class Meta:
        model = Character
        fields = ("name", "magical", "sex", "creature", "school_attended", "house")
        attrs = {"class": "table table-striped table-bordered table-hover"}
