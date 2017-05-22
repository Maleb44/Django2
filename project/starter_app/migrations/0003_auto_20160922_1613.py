# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starter_app', '0002_auto_20160910_1215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='order',
        ),
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.CharField(default=b'SOME STRING', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, editable=False),
        ),
    ]
