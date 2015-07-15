# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table(u'main_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Genre'])

        # Adding model 'Year'
        db.create_table(u'main_year', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Year'])

        # Adding unique constraint on 'Actor', fields ['name']
        db.create_unique(u'main_actor', ['name'])

        # Adding unique constraint on 'Actress', fields ['name']
        db.create_unique(u'main_actress', ['name'])

        # Adding unique constraint on 'Director', fields ['name']
        db.create_unique(u'main_director', ['name'])


        # Renaming column for 'Film.year' to match new field type.
        db.rename_column(u'main_film', 'year', 'year_id')
        # Changing field 'Film.year'
        db.alter_column(u'main_film', 'year_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Year'], null=True))
        # Adding index on 'Film', fields ['year']
        db.create_index(u'main_film', ['year_id'])


        # Renaming column for 'Film.genre' to match new field type.
        db.rename_column(u'main_film', 'genre', 'genre_id')
        # Changing field 'Film.genre'
        db.alter_column(u'main_film', 'genre_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Genre'], null=True))
        # Adding index on 'Film', fields ['genre']
        db.create_index(u'main_film', ['genre_id'])


    def backwards(self, orm):
        # Removing index on 'Film', fields ['genre']
        db.delete_index(u'main_film', ['genre_id'])

        # Removing index on 'Film', fields ['year']
        db.delete_index(u'main_film', ['year_id'])

        # Removing unique constraint on 'Director', fields ['name']
        db.delete_unique(u'main_director', ['name'])

        # Removing unique constraint on 'Actress', fields ['name']
        db.delete_unique(u'main_actress', ['name'])

        # Removing unique constraint on 'Actor', fields ['name']
        db.delete_unique(u'main_actor', ['name'])

        # Deleting model 'Genre'
        db.delete_table(u'main_genre')

        # Deleting model 'Year'
        db.delete_table(u'main_year')


        # Renaming column for 'Film.year' to match new field type.
        db.rename_column(u'main_film', 'year_id', 'year')
        # Changing field 'Film.year'
        db.alter_column(u'main_film', 'year', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Renaming column for 'Film.genre' to match new field type.
        db.rename_column(u'main_film', 'genre_id', 'genre')
        # Changing field 'Film.genre'
        db.alter_column(u'main_film', 'genre', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    models = {
        u'main.actor': {
            'Meta': {'object_name': 'Actor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'main.actress': {
            'Meta': {'object_name': 'Actress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'main.director': {
            'Meta': {'object_name': 'Director'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'main.film': {
            'Meta': {'object_name': 'Film'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Actor']", 'null': 'True'}),
            'actress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Actress']", 'null': 'True'}),
            'awards': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Director']", 'null': 'True'}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Genre']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popularity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Year']", 'null': 'True'})
        },
        u'main.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.year': {
            'Meta': {'object_name': 'Year'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']