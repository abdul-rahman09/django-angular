# Generated by Django 2.1.5 on 2019-03-09 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lawyer', '0007_auto_20190309_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawyer',
            name='fields',
        ),
    ]
