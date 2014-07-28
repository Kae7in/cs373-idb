# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'House.quote'
        db.alter_column('marauder_house', 'quote', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'House.quote'
        db.alter_column('marauder_house', 'quote', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        'marauder.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['marauder.Character']", 'null': 'True', 'related_name': "'artifacts'"}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Shop']", 'null': 'True', 'related_name': "'artifacts'"})
        },
        'marauder.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Character']", 'null': 'True', 'related_name': "'books_published'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'published_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['marauder.Character']", 'null': 'True', 'related_name': "'books_starred'"})
        },
        'marauder.character': {
            'Meta': {'object_name': 'Character'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Creature']", 'null': 'True', 'related_name': "'characters'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.House']", 'null': 'True', 'related_name': "'members'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'magical': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'quote_by': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_attended': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'students'"}),
            'school_founded': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'founders'"}),
            'school_headmastered': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'headmasters'"}),
            'school_staffed': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'staff'"}),
            'school_taught': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'professors'"}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Shop']", 'null': 'True', 'related_name': "'owners'"}),
            'wand': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'marauder.creature': {
            'Meta': {'object_name': 'Creature'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notable': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'plural': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': '0'})
        },
        'marauder.house': {
            'Meta': {'object_name': 'House', '_ormbases': ['marauder.School']},
            'colors': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'founder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'house_founded'", 'to': "orm['marauder.Character']"}),
            'ghost': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'houses_haunted'", 'to': "orm['marauder.Character']"}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'quote_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'houses'", 'to': "orm['marauder.School']"}),
            'school_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marauder.School']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marauder.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Creature']", 'null': 'True', 'related_name': "'ingredients'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.location': {
            'Meta': {'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.potion': {
            'Meta': {'object_name': 'Potion'},
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'effects': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['marauder.Ingredient']", 'null': 'True', 'related_name': "'potions'"}),
            'notable_uses': ('django.db.models.fields.TextField', [], {}),
            'physical_description': ('django.db.models.fields.TextField', [], {}),
            'recipe': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'character1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Character']", 'null': 'True', 'related_name': "'relationships1'"}),
            'character2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Character']", 'null': 'True', 'related_name': "'relationships2'"}),
            'descriptor1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'descriptor2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'marauder.school': {
            'Meta': {'object_name': 'School', '_ormbases': ['marauder.Location']},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marauder.Location']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marauder.shop': {
            'Meta': {'object_name': 'Shop', '_ormbases': ['marauder.Location']},
            'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marauder.Location']", 'unique': 'True', 'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['marauder.Location']", 'null': 'True', 'related_name': "'shops'"})
        },
        'marauder.spell': {
            'Meta': {'object_name': 'Spell'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Creature']", 'null': 'True', 'related_name': "'spells'"}),
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
            'artifacts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'stories'", 'symmetrical': 'False', 'to': "orm['marauder.Artifact']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Book']", 'null': 'True', 'related_name': "'story'"}),
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'stories'", 'symmetrical': 'False', 'to': "orm['marauder.Character']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'stories'", 'symmetrical': 'False', 'to': "orm['marauder.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['marauder']