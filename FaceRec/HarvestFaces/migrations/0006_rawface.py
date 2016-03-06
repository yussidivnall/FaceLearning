# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRec', '__first__'),
        ('HarvestFaces', '0005_auto_20160306_0510'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawFace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'raw')),
                ('person', models.ForeignKey(to='FaceRec.Person', null=True)),
                ('src', models.ManyToManyField(to='HarvestFaces.RawImage')),
            ],
        ),
    ]
