# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_department_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='right',
            name='slug',
            field=models.SlugField(default='null-right'),
            preserve_default=False,
        ),
    ]
