# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_gamereview_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamereview',
            name='estado',
            field=models.CharField(default='asd', max_length=50),
            preserve_default=False,
        ),
    ]
