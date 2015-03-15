# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20150307_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='person',
            name='firstname',
            field=models.CharField(max_length=100, default='Vorname'),
            preserve_default=False,
        ),
    ]
