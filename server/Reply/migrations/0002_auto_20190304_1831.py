# Generated by Django 2.1.5 on 2019-03-04 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quest', to='Question.Question'),
        ),
    ]
