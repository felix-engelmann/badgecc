# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20150308_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='color',
            field=models.CharField(max_length=30, default='black'),
            preserve_default=False,
        ),
    ]
