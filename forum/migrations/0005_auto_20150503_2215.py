# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20150430_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='cat',
            field=models.ForeignKey(blank=True, to='forum.Categoria', null=True),
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='text',
            field=models.TextField(),
        ),
    ]
