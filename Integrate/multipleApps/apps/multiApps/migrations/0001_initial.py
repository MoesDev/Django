# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logins', '0002_auto_20161114_1700'),
        ('the_courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='the_courses.Course')),
                ('user_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='logins.User')),
            ],
        ),
    ]
