# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarvestFaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawimage',
            name='notes',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='rawimage',
            name='person_hints',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
