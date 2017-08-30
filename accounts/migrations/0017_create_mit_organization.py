# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 19:20
from __future__ import unicode_literals

from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations

from accounts.models import Organization

# THIS IS A NOOP BECAUSE IT'S REPLACED WITH A SIGNAL HANDLER AND IT'S
# VERY DIFFICULT TO REMOVE IN ANOTHER WAY


def create_mit_organization(apps, schema_editor, *args, **kwargs):
    pass


def remove_mit_organization(*args, **kwargs):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '__latest__'),
        ('sites', '__latest__'),
        ('accounts', '0016_auto_20170802_2311'),
    ]

    operations = [
        migrations.RunPython(create_mit_organization, remove_mit_organization)
    ]