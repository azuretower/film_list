# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Film'
        db.create_table(u'main_film', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('length', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('popularity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('awards', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('director', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Director'])),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Actor'])),
            ('actress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Actress'])),
        ))
        db.send_create_signal(u'main', ['Film'])

        # Adding model 'Director'
        db.create_table(u'main_director', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Director'])

        # Adding model 'Actor'
        db.create_table(u'main_actor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Actor'])

        # Adding model 'Actress'
        db.create_table(u'main_actress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Actress'])


    def backwards(self, orm):
        # Deleting model 'Film'
        db.delete_table(u'main_film')

        # Deleting model 'Director'
        db.delete_table(u'main_director')

        # Deleting model 'Actor'
        db.delete_table(u'main_actor')

        # Deleting model 'Actress'
        db.delete_table(u'main_actress')


    models = {
        u'main.actor': {
            'Meta': {'object_name': 'Actor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.actress': {
            'Meta': {'object_name': 'Actress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.director': {
            'Meta': {'object_name': 'Director'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.film': {
            'Meta': {'object_name': 'Film'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Actor']"}),
            'actress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Actress']"}),
            'awards': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Director']"}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popularity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']