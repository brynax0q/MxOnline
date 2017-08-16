# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-11 19:58
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_lesson_learn_times'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u8bfe\u7a0b',
                'proxy': True,
                'verbose_name_plural': '\u8f6e\u64ad\u8bfe\u7a0b',
            },
            bases=('courses.course',),
        ),
        migrations.RenameField(
            model_name='course',
            old_name='category',
            new_name='categroy',
        ),
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u8bfe\u7a0b\u8be6\u60c5'),
        ),
    ]
