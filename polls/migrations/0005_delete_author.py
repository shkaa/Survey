# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
