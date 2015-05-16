# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_denuncia'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='review',
            field=models.ForeignKey(to='forum.Gamereview', null=True),
        ),
    ]
