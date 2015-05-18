# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_denuncia'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamereview',
            name='estado',
            field=models.CharField(default='publicado', max_length=50),
            preserve_default=False,
        ),
    ]
