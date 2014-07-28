# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field artifacts on 'Story'
        db.delete_table(db.shorten_name('marauder_story_artifacts'))


    def backwards(self, orm):
        # Adding M2M table for field artifacts on 'Story'
        m2m_table_name = db.shorten_name('marauder_story_artifacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['marauder.story'], null=False)),
            ('artifact', models.ForeignKey(orm['marauder.artifact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['story_id', 'artifact_id'])


    models = {
        'marauder.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Character']", 'related_name': "'artifacts'", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Shop']", 'null': 'True', 'related_name': "'artifacts'", 'blank': 'True'})
        },
        'marauder.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Character']", 'null': 'True', 'related_name': "'books_published'", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'published_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Character']", 'related_name': "'books_starred'", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'})
        },
        'marauder.character': {
            'Meta': {'object_name': 'Character'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Creature']", 'null': 'True', 'related_name': "'characters'", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.House']", 'null': 'True', 'related_name': "'members'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'magical': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'quote_by': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_attended': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'students'", 'blank': 'True'}),
            'school_founded': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'founders'", 'blank': 'True'}),
            'school_headmastered': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'headmasters'", 'blank': 'True'}),
            'school_staffed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'staff'", 'blank': 'True'}),
            'school_taught': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.School']", 'null': 'True', 'related_name': "'professors'", 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Shop']", 'null': 'True', 'related_name': "'owners'", 'blank': 'True'}),
            'wand': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '150'})
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
            'Meta': {'_ormbases': ['marauder.School'], 'object_name': 'House'},
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
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Creature']", 'null': 'True', 'related_name': "'ingredients'", 'blank': 'True'}),
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
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Ingredient']", 'related_name': "'potions'", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'notable_uses': ('django.db.models.fields.TextField', [], {}),
            'physical_description': ('django.db.models.fields.TextField', [], {}),
            'recipe': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'character1': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Character']", 'null': 'True', 'related_name': "'relationships1'", 'blank': 'True'}),
            'character2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Character']", 'null': 'True', 'related_name': "'relationships2'", 'blank': 'True'}),
            'descriptor1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'descriptor2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'marauder.school': {
            'Meta': {'_ormbases': ['marauder.Location'], 'object_name': 'School'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marauder.Location']", 'primary_key': 'True', 'unique': 'True'})
        },
        'marauder.shop': {
            'Meta': {'_ormbases': ['marauder.Location'], 'object_name': 'Shop'},
            'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marauder.Location']", 'primary_key': 'True', 'unique': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Location']", 'related_name': "'shops'", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'})
        },
        'marauder.spell': {
            'Meta': {'object_name': 'Spell'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Creature']", 'null': 'True', 'related_name': "'spells'", 'blank': 'True'}),
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
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['marauder.Book']", 'null': 'True', 'related_name': "'story'", 'blank': 'True'}),
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Character']", 'related_name': "'stories'", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['marauder.Location']", 'related_name': "'stories'", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quote_by': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['marauder']