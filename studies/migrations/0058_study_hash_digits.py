# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-01-08 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("studies", "0057_study_remove_null_salt")]

    operations = [
        migrations.AddField(
            model_name="study", name="hash_digits", field=models.IntegerField(default=6)
        )
    ]
