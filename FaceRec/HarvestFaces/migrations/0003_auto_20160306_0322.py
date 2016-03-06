# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HarvestFaces', '0002_auto_20160111_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rawimage',
            old_name='notes',
            new_name='tags',
        ),
        migrations.RemoveField(
            model_name='rawimage',
            name='person_hints',
        ),
    ]
