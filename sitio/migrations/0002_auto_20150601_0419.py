# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fecha',
            field=models.DateTimeField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default=b'sitio/static/img/defaultuser.jpg', upload_to=b'web'),
        ),
    ]
