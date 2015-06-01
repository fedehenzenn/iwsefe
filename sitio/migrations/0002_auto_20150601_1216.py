# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='apellido',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fecha_alta',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 12, 15, 40, 723665, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default=b'sitio/static/img/defaultuser.jpg', upload_to=b'web'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nombre',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
