# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import project.fields.datetime_aware_jsonfield


class Migration(migrations.Migration):

    dependencies = [("studies", "0044_unified_ember_app")]

    operations = [
        migrations.AddField(
            model_name="study",
            name="compensation_description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="consentruling",
            name="action",
            field=models.CharField(
                choices=[
                    ("accepted", "accepted"),
                    ("rejected", "rejected"),
                    ("pending", "pending"),
                ],
                db_index=True,
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="studytype",
            name="configuration",
            field=project.fields.datetime_aware_jsonfield.DateTimeAwareJSONField(
                default={
                    "metadata": {
                        "fields": {
                            "last_known_player_sha": None,
                            "player_repo_url": "https://github.com/lookit/ember-lookit-frameplayer",
                        }
                    },
                    "task_module": "studies.tasks",
                }
            ),
        ),
    ]
