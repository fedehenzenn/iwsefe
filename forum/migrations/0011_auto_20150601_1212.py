# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20150601_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
