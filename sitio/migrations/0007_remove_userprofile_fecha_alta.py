# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0006_auto_20150627_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='fecha_alta',
        ),
    ]
