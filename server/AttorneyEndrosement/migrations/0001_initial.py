# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 12:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0003_auto_20190507_1530'),
        ('Lawyer', '0009_auto_20190507_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttorneyEndrosement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('isHired', models.BooleanField(default=True)),
                ('isRecomended', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('fromLawyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Lawyer.Lawyer')),
                ('toLawyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Client.Client')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='attorneyendrosement',
            unique_together=set([('fromLawyer', 'toLawyer')]),
        ),
    ]
