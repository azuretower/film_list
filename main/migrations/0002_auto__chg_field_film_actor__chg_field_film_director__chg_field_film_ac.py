# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Film.actor'
        db.alter_column(u'main_film', 'actor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Actor'], null=True))

        # Changing field 'Film.director'
        db.alter_column(u'main_film', 'director_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Director'], null=True))

        # Changing field 'Film.actress'
        db.alter_column(u'main_film', 'actress_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Actress'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Film.actor'
        raise RuntimeError("Cannot reverse this migration. 'Film.actor' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Film.actor'
        db.alter_column(u'main_film', 'actor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Actor']))

        # User chose to not deal with backwards NULL issues for 'Film.director'
        raise RuntimeError("Cannot reverse this migration. 'Film.director' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Film.director'
        db.alter_column(u'main_film', 'director_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Director']))

        # User chose to not deal with backwards NULL issues for 'Film.actress'
        raise RuntimeError("Cannot reverse this migration. 'Film.actress' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Film.actress'
        db.alter_column(u'main_film', 'actress_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Actress']))

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
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Actor']", 'null': 'True'}),
            'actress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Actress']", 'null': 'True'}),
            'awards': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Director']", 'null': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popularity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']