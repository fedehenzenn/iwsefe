# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0003_auto_20150622_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='fecha_alta',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 27, 20, 21, 32, 237869, tzinfo=utc)),
        ),
    ]
