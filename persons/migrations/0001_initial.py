# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('background', models.ImageField(upload_to='')),
                ('default_image', models.ImageField(upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('printed', models.BooleanField(default=False)),
                ('department', models.ForeignKey(to='persons.Department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rights', models.ManyToManyField(to='persons.Right')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='extra_rights',
            field=models.ManyToManyField(to='persons.Right'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(to='persons.Role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='rights',
            field=models.ManyToManyField(to='persons.Right'),
            preserve_default=True,
        ),
    ]
