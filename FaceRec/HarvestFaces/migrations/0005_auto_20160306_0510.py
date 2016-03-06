# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HarvestFaces', '0004_rawimage_session_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rawimage',
            old_name='session_id',
            new_name='harvest_id',
        ),
    ]
