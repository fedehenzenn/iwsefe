# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_auto_20150601_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereview',
            name='text',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
