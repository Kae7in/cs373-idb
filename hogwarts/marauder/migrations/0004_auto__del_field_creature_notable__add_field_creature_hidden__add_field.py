# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Creature.notable'
        db.delete_column('marauder_creature', 'notable')

        # Adding field 'Creature.hidden'
        db.add_column('marauder_creature', 'hidden',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.hidden'
        db.add_column('marauder_character', 'hidden',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Spell.difficulty'
        db.add_column('marauder_spell', 'difficulty',
                      self.gf('django.db.models.fields.CharField')(default='Easy', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Creature.notable'
        db.add_column('marauder_creature', 'notable',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Creature.hidden'
        db.delete_column('marauder_creature', 'hidden')

        # Deleting field 'Character.hidden'
        db.delete_column('marauder_character', 'hidden')

        # Deleting field 'Spell.difficulty'
        db.delete_column('marauder_spell', 'difficulty')


    models = {
        'marauder.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'null': 'True', 'related_name': "'artifacts'", 'to': "orm['marauder.Character']"}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'artifacts'", 'to': "orm['marauder.Shop']"})
        },
        'marauder.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'books_published'", 'to': "orm['marauder.Character']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'published_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'null': 'True', 'related_name': "'books_starred'", 'to': "orm['marauder.Character']"})
        },
        'marauder.character': {
            'Meta': {'object_name': 'Character'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'characters'", 'to': "orm['marauder.Creature']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'members'", 'to': "orm['marauder.House']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'magical': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'quote_by': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_attended': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'students'", 'to': "orm['marauder.School']"}),
            'school_founded': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'founders'", 'to': "orm['marauder.School']"}),
            'school_headmastered': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'headmasters'", 'to': "orm['marauder.School']"}),
            'school_staffed': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'staff'", 'to': "orm['marauder.School']"}),
            'school_taught': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'professors'", 'to': "orm['marauder.School']"}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'owners'", 'to': "orm['marauder.Shop']"}),
            'wand': ('django.db.models.fields.CharField', [], {'max_length': '150'})
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
            'rating': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': '0'})
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
            'school_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marauder.School']", 'primary_key': 'True', 'unique': 'True'})
        },
        'marauder.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'ingredients'", 'to': "orm['marauder.Creature']"}),
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
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'null': 'True', 'related_name': "'potions'", 'to': "orm['marauder.Ingredient']"}),
            'notable_uses': ('django.db.models.fields.TextField', [], {}),
            'physical_description': ('django.db.models.fields.TextField', [], {}),
            'recipe': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'character1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'relationships1'", 'to': "orm['marauder.Character']"}),
            'character2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'relationships2'", 'to': "orm['marauder.Character']"}),
            'descriptor1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'descriptor2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'marauder.school': {
            'Meta': {'object_name': 'School', '_ormbases': ['marauder.Location']},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marauder.Location']", 'primary_key': 'True', 'unique': 'True'})
        },
        'marauder.shop': {
            'Meta': {'object_name': 'Shop', '_ormbases': ['marauder.Location']},
            'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marauder.Location']", 'primary_key': 'True', 'unique': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'null': 'True', 'related_name': "'shops'", 'to': "orm['marauder.Location']"})
        },
        'marauder.spell': {
            'Meta': {'object_name': 'Spell'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'spells'", 'to': "orm['marauder.Creature']"}),
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
            'artifacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Artifact']", 'symmetrical': 'False', 'related_name': "'stories'"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'related_name': "'story'", 'to': "orm['marauder.Book']"}),
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Character']", 'symmetrical': 'False', 'related_name': "'stories'"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Location']", 'symmetrical': 'False', 'related_name': "'stories'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['marauder']