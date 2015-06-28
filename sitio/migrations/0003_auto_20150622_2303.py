# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0002_auto_20150601_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='fecha_alta',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 23, 3, 38, 760530, tzinfo=utc)),
        ),
    ]
