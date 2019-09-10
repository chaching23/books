# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-18 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_authors_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='books',
            field=models.ManyToManyField(related_name='Authors', to='first_app.Books'),
        ),
    ]
