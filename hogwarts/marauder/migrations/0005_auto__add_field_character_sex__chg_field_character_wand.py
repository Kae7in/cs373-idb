# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Character.sex'
        db.add_column('marauder_character', 'sex',
                      self.gf('django.db.models.fields.CharField')(default='NB', max_length=2),
                      keep_default=False)


        # Changing field 'Character.wand'
        db.alter_column('marauder_character', 'wand', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

    def backwards(self, orm):
        # Deleting field 'Character.sex'
        db.delete_column('marauder_character', 'sex')


        # Changing field 'Character.wand'
        db.alter_column('marauder_character', 'wand', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=150))

    models = {
        'marauder.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'artifacts'", 'to': "orm['marauder.Character']", 'symmetrical': 'False', 'null': 'True', 'blank': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artifacts'", 'to': "orm['marauder.Shop']", 'null': 'True', 'blank': 'True'})
        },
        'marauder.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'books_published'", 'to': "orm['marauder.Character']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'published_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'books_starred'", 'to': "orm['marauder.Character']", 'symmetrical': 'False', 'null': 'True', 'blank': 'True'})
        },
        'marauder.character': {
            'Meta': {'object_name': 'Character'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['marauder.Creature']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'to': "orm['marauder.House']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'magical': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'quote_by': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_attended': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'to': "orm['marauder.School']", 'null': 'True', 'blank': 'True'}),
            'school_founded': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'founders'", 'to': "orm['marauder.School']", 'null': 'True', 'blank': 'True'}),
            'school_headmastered': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'headmasters'", 'to': "orm['marauder.School']", 'null': 'True', 'blank': 'True'}),
            'school_staffed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'staff'", 'to': "orm['marauder.School']", 'null': 'True', 'blank': 'True'}),
            'school_taught': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'professors'", 'to': "orm['marauder.School']", 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owners'", 'to': "orm['marauder.Shop']", 'null': 'True', 'blank': 'True'}),
            'wand': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
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
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ingredients'", 'to': "orm['marauder.Creature']", 'null': 'True', 'blank': 'True'}),
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
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'potions'", 'to': "orm['marauder.Ingredient']", 'symmetrical': 'False', 'null': 'True', 'blank': 'True'}),
            'notable_uses': ('django.db.models.fields.TextField', [], {}),
            'physical_description': ('django.db.models.fields.TextField', [], {}),
            'recipe': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'character1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relationships1'", 'to': "orm['marauder.Character']", 'null': 'True', 'blank': 'True'}),
            'character2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relationships2'", 'to': "orm['marauder.Character']", 'null': 'True', 'blank': 'True'}),
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
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'shops'", 'to': "orm['marauder.Location']", 'symmetrical': 'False', 'null': 'True', 'blank': 'True'})
        },
        'marauder.spell': {
            'Meta': {'object_name': 'Spell'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'spells'", 'to': "orm['marauder.Creature']", 'null': 'True', 'blank': 'True'}),
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
            'artifacts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'stories'", 'to': "orm['marauder.Artifact']", 'symmetrical': 'False'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'story'", 'to': "orm['marauder.Book']", 'null': 'True', 'blank': 'True'}),
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'stories'", 'to': "orm['marauder.Character']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'stories'", 'to': "orm['marauder.Location']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['marauder']