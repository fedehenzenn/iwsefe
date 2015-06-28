# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0011_auto_20150601_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='puntuacion',
            name='review',
        ),
        migrations.RemoveField(
            model_name='puntuacion',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.DeleteModel(
            name='Puntuacion',
        ),
        migrations.AddField(
            model_name='voto',
            name='review',
            field=models.ForeignKey(to='forum.Gamereview'),
        ),
    ]
