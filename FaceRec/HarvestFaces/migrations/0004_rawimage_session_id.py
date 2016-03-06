# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HarvestFaces', '0003_auto_20160306_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawimage',
            name='session_id',
            field=models.IntegerField(null=True),
        ),
    ]
