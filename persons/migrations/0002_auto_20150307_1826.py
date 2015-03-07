# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='default_image',
            field=models.ImageField(upload_to='', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='rights',
            field=models.ManyToManyField(to='persons.Right', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='extra_rights',
            field=models.ManyToManyField(to='persons.Right', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.ForeignKey(to='persons.Role', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='rights',
            field=models.ManyToManyField(to='persons.Right', blank=True, null=True),
            preserve_default=True,
        ),
    ]
