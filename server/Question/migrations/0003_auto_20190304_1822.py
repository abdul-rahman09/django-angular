# Generated by Django 2.1.5 on 2019-03-04 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0002_auto_20190227_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.Client'),
        ),
    ]
