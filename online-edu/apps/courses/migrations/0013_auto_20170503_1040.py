# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-03 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_course_alldesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='learned_times',
            field=models.CharField(max_length=100, verbose_name='\u5b66\u4e60\u65f6\u957f(\u5206\u949f\u6570)'),
        ),
    ]