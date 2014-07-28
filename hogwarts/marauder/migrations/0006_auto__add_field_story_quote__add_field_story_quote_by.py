# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Story.quote'
        db.add_column('marauder_story', 'quote',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Story.quote_by'
        db.add_column('marauder_story', 'quote_by',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Story.quote'
        db.delete_column('marauder_story', 'quote')

        # Deleting field 'Story.quote_by'
        db.delete_column('marauder_story', 'quote_by')


    models = {
        'marauder.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'images/empty.jpg'"}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'artifacts'", 'to': "orm['marauder.Character']", 'blank': 'True', 'symmetrical': 'False'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.Shop']", 'blank': 'True', 'related_name': "'artifacts'"})
        },
        'marauder.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.Character']", 'blank': 'True', 'related_name': "'books_published'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'images/empty.jpg'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'published_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'books_starred'", 'to': "orm['marauder.Character']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'marauder.character': {
            'Meta': {'object_name': 'Character'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.Creature']", 'blank': 'True', 'related_name': "'characters'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.House']", 'blank': 'True', 'related_name': "'members'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'images/empty.jpg'"}),
            'magical': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'quote_by': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_attended': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.School']", 'blank': 'True', 'related_name': "'students'"}),
            'school_founded': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.School']", 'blank': 'True', 'related_name': "'founders'"}),
            'school_headmastered': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.School']", 'blank': 'True', 'related_name': "'headmasters'"}),
            'school_staffed': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.School']", 'blank': 'True', 'related_name': "'staff'"}),
            'school_taught': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.School']", 'blank': 'True', 'related_name': "'professors'"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.Shop']", 'blank': 'True', 'related_name': "'owners'"}),
            'wand': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '150', 'blank': 'True'})
        },
        'marauder.creature': {
            'Meta': {'object_name': 'Creature'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'plural': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'marauder.house': {
            'Meta': {'object_name': 'House', '_ormbases': ['marauder.School']},
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'founder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Character']", 'related_name': "'house_founded'"}),
            'ghost': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Character']", 'related_name': "'houses_haunted'"}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'quote_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.School']", 'related_name': "'houses'"}),
            'school_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['marauder.School']", 'primary_key': 'True'})
        },
        'marauder.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.Creature']", 'blank': 'True', 'related_name': "'ingredients'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.location': {
            'Meta': {'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'images/empty.jpg'"}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.potion': {
            'Meta': {'object_name': 'Potion'},
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'effects': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'images/empty.jpg'"}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'potions'", 'to': "orm['marauder.Ingredient']", 'blank': 'True', 'symmetrical': 'False'}),
            'notable_uses': ('django.db.models.fields.TextField', [], {}),
            'physical_description': ('django.db.models.fields.TextField', [], {}),
            'recipe': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'character1': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.Character']", 'blank': 'True', 'related_name': "'relationships1'"}),
            'character2': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.Character']", 'blank': 'True', 'related_name': "'relationships2'"}),
            'descriptor1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'descriptor2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'marauder.school': {
            'Meta': {'object_name': 'School', '_ormbases': ['marauder.Location']},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['marauder.Location']", 'primary_key': 'True'})
        },
        'marauder.shop': {
            'Meta': {'object_name': 'Shop', '_ormbases': ['marauder.Location']},
            'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['marauder.Location']", 'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'shops'", 'to': "orm['marauder.Location']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'marauder.spell': {
            'Meta': {'object_name': 'Spell'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.Creature']", 'blank': 'True', 'related_name': "'spells'"}),
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'effect': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'incantation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'notable_uses': ('django.db.models.fields.TextField', [], {}),
            'unforgivable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'marauder.story': {
            'Meta': {'object_name': 'Story'},
            'artifacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Artifact']", 'related_name': "'stories'", 'symmetrical': 'False'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['marauder.Book']", 'blank': 'True', 'related_name': "'story'"}),
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Character']", 'related_name': "'stories'", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'images/empty.jpg'"}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'stories'", 'to': "orm['marauder.Location']", 'blank': 'True', 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quote_by': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['marauder']