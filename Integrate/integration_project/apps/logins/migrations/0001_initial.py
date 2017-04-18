# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
