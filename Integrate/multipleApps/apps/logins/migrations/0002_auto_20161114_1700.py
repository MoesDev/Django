# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 23:00
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('usermanager', django.db.models.manager.Manager()),
            ],
        ),
    ]
