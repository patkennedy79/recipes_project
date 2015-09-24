# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('rating', models.PositiveIntegerField(default=1)),
                ('recipe_type', models.CharField(default='DI', choices=[('BR', 'Breakfast'), ('LU', 'Lunch'), ('DI', 'Dinner'), ('DE', 'Dessert')], max_length=2)),
                ('recipe_steps', models.TextField(default='Add recipe steps!')),
                ('ingredients', models.TextField(default='Add ingredients!')),
            ],
        ),
    ]
