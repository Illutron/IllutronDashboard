# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Provider'
        db.create_table('log_provider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('log', ['Provider'])

        # Adding model 'Entry'
        db.create_table('log_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('on_illutron', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=6, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=6, blank=True)),
            ('accuracy', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['log.Provider'])),
        ))
        db.send_create_signal('log', ['Entry'])

        # Adding M2M table for field member on 'Entry'
        db.create_table('log_entry_member', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['log.entry'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('log_entry_member', ['entry_id', 'user_id'])


    def backwards(self, orm):
        
        # Deleting model 'Provider'
        db.delete_table('log_provider')

        # Deleting model 'Entry'
        db.delete_table('log_entry')

        # Removing M2M table for field member on 'Entry'
        db.delete_table('log_entry_member')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'log.entry': {
            'Meta': {'object_name': 'Entry'},
            'accuracy': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'on_illutron': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['log.Provider']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'log.provider': {
            'Meta': {'object_name': 'Provider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['log']
