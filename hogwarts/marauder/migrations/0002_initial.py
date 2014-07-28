# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Character'
        db.create_table('marauder_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('wand', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('magical', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('quote', self.gf('django.db.models.fields.TextField')()),
            ('quote_by', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='images/empty.jpg', max_length=100)),
            ('creature', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.Creature'], related_name='characters', null=True)),
            ('house', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.House'], related_name='members', null=True)),
            ('school_attended', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.School'], related_name='students', null=True)),
            ('school_taught', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.School'], related_name='professors', null=True)),
            ('school_headmastered', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.School'], related_name='headmasters', null=True)),
            ('school_founded', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.School'], related_name='founders', null=True)),
            ('school_staffed', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.School'], related_name='staff', null=True)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.Shop'], related_name='owners', null=True)),
        ))
        db.send_create_signal('marauder', ['Character'])

        # Adding model 'Creature'
        db.create_table('marauder_creature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('plural', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('classification', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('notable', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(blank=True, default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('marauder', ['Creature'])

        # Adding model 'Spell'
        db.create_table('marauder_spell', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('incantation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('effect', self.gf('django.db.models.fields.TextField')()),
            ('creator', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('notable_uses', self.gf('django.db.models.fields.TextField')()),
            ('unforgivable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('creature', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.Creature'], related_name='spells', null=True)),
        ))
        db.send_create_signal('marauder', ['Spell'])

        # Adding model 'Ingredient'
        db.create_table('marauder_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('creature', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.Creature'], related_name='ingredients', null=True)),
        ))
        db.send_create_signal('marauder', ['Ingredient'])

        # Adding model 'Potion'
        db.create_table('marauder_potion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('difficulty', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('effects', self.gf('django.db.models.fields.TextField')()),
            ('recipe', self.gf('django.db.models.fields.TextField')()),
            ('notable_uses', self.gf('django.db.models.fields.TextField')()),
            ('physical_description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='images/empty.jpg', max_length=100)),
        ))
        db.send_create_signal('marauder', ['Potion'])

        # Adding M2M table for field ingredients on 'Potion'
        m2m_table_name = db.shorten_name('marauder_potion_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('potion', models.ForeignKey(orm['marauder.potion'], null=False)),
            ('ingredient', models.ForeignKey(orm['marauder.ingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['potion_id', 'ingredient_id'])

        # Adding model 'Location'
        db.create_table('marauder_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='images/empty.jpg', max_length=100)),
        ))
        db.send_create_signal('marauder', ['Location'])

        # Adding model 'School'
        db.create_table('marauder_school', (
            ('location_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marauder.Location'], unique=True, primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('marauder', ['School'])

        # Adding model 'House'
        db.create_table('marauder_house', (
            ('school_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marauder.School'], unique=True, primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(related_name='houses', to=orm['marauder.School'])),
            ('ghost', self.gf('django.db.models.fields.related.ForeignKey')(related_name='houses_haunted', to=orm['marauder.Character'])),
            ('colors', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mascot', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('quote', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('quote_by', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('founder', self.gf('django.db.models.fields.related.ForeignKey')(related_name='house_founded', to=orm['marauder.Character'])),
        ))
        db.send_create_signal('marauder', ['House'])

        # Adding model 'Shop'
        db.create_table('marauder_shop', (
            ('location_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['marauder.Location'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('marauder', ['Shop'])

        # Adding M2M table for field locations on 'Shop'
        m2m_table_name = db.shorten_name('marauder_shop_locations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('shop', models.ForeignKey(orm['marauder.shop'], null=False)),
            ('location', models.ForeignKey(orm['marauder.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['shop_id', 'location_id'])

        # Adding model 'Artifact'
        db.create_table('marauder_artifact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('kind', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='images/empty.jpg', max_length=100)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.Shop'], related_name='artifacts', null=True)),
        ))
        db.send_create_signal('marauder', ['Artifact'])

        # Adding M2M table for field owners on 'Artifact'
        m2m_table_name = db.shorten_name('marauder_artifact_owners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artifact', models.ForeignKey(orm['marauder.artifact'], null=False)),
            ('character', models.ForeignKey(orm['marauder.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['artifact_id', 'character_id'])

        # Adding model 'Book'
        db.create_table('marauder_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.Character'], related_name='books_published', null=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=200)),
            ('published_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='images/empty.jpg', max_length=100)),
        ))
        db.send_create_signal('marauder', ['Book'])

        # Adding M2M table for field subjects on 'Book'
        m2m_table_name = db.shorten_name('marauder_book_subjects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['marauder.book'], null=False)),
            ('character', models.ForeignKey(orm['marauder.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'character_id'])

        # Adding model 'Story'
        db.create_table('marauder_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.Book'], related_name='story', null=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='images/empty.jpg', max_length=100)),
        ))
        db.send_create_signal('marauder', ['Story'])

        # Adding M2M table for field characters on 'Story'
        m2m_table_name = db.shorten_name('marauder_story_characters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['marauder.story'], null=False)),
            ('character', models.ForeignKey(orm['marauder.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['story_id', 'character_id'])

        # Adding M2M table for field artifacts on 'Story'
        m2m_table_name = db.shorten_name('marauder_story_artifacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['marauder.story'], null=False)),
            ('artifact', models.ForeignKey(orm['marauder.artifact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['story_id', 'artifact_id'])

        # Adding M2M table for field locations on 'Story'
        m2m_table_name = db.shorten_name('marauder_story_locations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['marauder.story'], null=False)),
            ('location', models.ForeignKey(orm['marauder.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['story_id', 'location_id'])

        # Adding model 'Relationship'
        db.create_table('marauder_relationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.Character'], related_name='relationships1', null=True)),
            ('character2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['marauder.Character'], related_name='relationships2', null=True)),
            ('descriptor1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descriptor2', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('marauder', ['Relationship'])


    def backwards(self, orm):
        # Deleting model 'Character'
        db.delete_table('marauder_character')

        # Deleting model 'Creature'
        db.delete_table('marauder_creature')

        # Deleting model 'Spell'
        db.delete_table('marauder_spell')

        # Deleting model 'Ingredient'
        db.delete_table('marauder_ingredient')

        # Deleting model 'Potion'
        db.delete_table('marauder_potion')

        # Removing M2M table for field ingredients on 'Potion'
        db.delete_table(db.shorten_name('marauder_potion_ingredients'))

        # Deleting model 'Location'
        db.delete_table('marauder_location')

        # Deleting model 'School'
        db.delete_table('marauder_school')

        # Deleting model 'House'
        db.delete_table('marauder_house')

        # Deleting model 'Shop'
        db.delete_table('marauder_shop')

        # Removing M2M table for field locations on 'Shop'
        db.delete_table(db.shorten_name('marauder_shop_locations'))

        # Deleting model 'Artifact'
        db.delete_table('marauder_artifact')

        # Removing M2M table for field owners on 'Artifact'
        db.delete_table(db.shorten_name('marauder_artifact_owners'))

        # Deleting model 'Book'
        db.delete_table('marauder_book')

        # Removing M2M table for field subjects on 'Book'
        db.delete_table(db.shorten_name('marauder_book_subjects'))

        # Deleting model 'Story'
        db.delete_table('marauder_story')

        # Removing M2M table for field characters on 'Story'
        db.delete_table(db.shorten_name('marauder_story_characters'))

        # Removing M2M table for field artifacts on 'Story'
        db.delete_table(db.shorten_name('marauder_story_artifacts'))

        # Removing M2M table for field locations on 'Story'
        db.delete_table(db.shorten_name('marauder_story_locations'))

        # Deleting model 'Relationship'
        db.delete_table('marauder_relationship')


    models = {
        'marauder.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'kind': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['marauder.Character']", 'related_name': "'artifacts'", 'null': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Shop']", 'related_name': "'artifacts'", 'null': 'True'})
        },
        'marauder.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Character']", 'related_name': "'books_published'", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'published_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['marauder.Character']", 'related_name': "'books_starred'", 'null': 'True'})
        },
        'marauder.character': {
            'Meta': {'object_name': 'Character'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Creature']", 'related_name': "'characters'", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.House']", 'related_name': "'members'", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/empty.jpg'", 'max_length': '100'}),
            'magical': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'quote_by': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_attended': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'related_name': "'students'", 'null': 'True'}),
            'school_founded': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'related_name': "'founders'", 'null': 'True'}),
            'school_headmastered': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'related_name': "'headmasters'", 'null': 'True'}),
            'school_staffed': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'related_name': "'staff'", 'null': 'True'}),
            'school_taught': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.School']", 'related_name': "'professors'", 'null': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Shop']", 'related_name': "'owners'", 'null': 'True'}),
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
            'quote': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'quote_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'houses'", 'to': "orm['marauder.School']"}),
            'school_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['marauder.School']", 'unique': 'True', 'primary_key': 'True'})
        },
        'marauder.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Creature']", 'related_name': "'ingredients'", 'null': 'True'}),
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
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['marauder.Ingredient']", 'related_name': "'potions'", 'null': 'True'}),
            'notable_uses': ('django.db.models.fields.TextField', [], {}),
            'physical_description': ('django.db.models.fields.TextField', [], {}),
            'recipe': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'marauder.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'character1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Character']", 'related_name': "'relationships1'", 'null': 'True'}),
            'character2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Character']", 'related_name': "'relationships2'", 'null': 'True'}),
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
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['marauder.Location']", 'related_name': "'shops'", 'null': 'True'})
        },
        'marauder.spell': {
            'Meta': {'object_name': 'Spell'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'creature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Creature']", 'related_name': "'spells'", 'null': 'True'}),
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
            'book': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['marauder.Book']", 'related_name': "'story'", 'null': 'True'}),
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