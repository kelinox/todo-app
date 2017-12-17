# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('todo_text', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('validate', models.BooleanField(default=False)),
            ],
        ),
    ]
