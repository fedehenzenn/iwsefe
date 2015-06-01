# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20150601_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 12, 6, 52, 937640)),
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 12, 6, 52, 937640)),
        ),
    ]
