# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_puntuacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 4, 32, 29, 550698)),
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 4, 32, 29, 550698)),
        ),
    ]
