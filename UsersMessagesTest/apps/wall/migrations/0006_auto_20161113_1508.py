# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 21:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0005_auto_20161111_1658'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
    ]
