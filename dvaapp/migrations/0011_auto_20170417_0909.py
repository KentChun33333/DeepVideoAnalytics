# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 09:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0010_cluster'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cluster',
            new_name='Clusters',
        ),
    ]
