# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0002_auto_20150601_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='apellido',
            field=models.TextField(default='asd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fecha_alta',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 4, 32, 29, 547147)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nombre',
            field=models.TextField(default='asd'),
            preserve_default=False,
        ),
    ]
