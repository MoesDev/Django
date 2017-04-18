# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0006_auto_20161113_1508'),
        ('integrate_projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='blog',
        ),
        migrations.AddField(
            model_name='test',
            name='blog_creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='wall.Message'),
        ),
        migrations.AddField(
            model_name='test',
            name='comment_creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='wall.Comment'),
        ),
        migrations.AlterField(
            model_name='test',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='user_creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='logins.User'),
        ),
    ]
