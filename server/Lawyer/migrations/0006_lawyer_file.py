# Generated by Django 2.1.5 on 2019-03-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lawyer', '0005_lawyer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='file',
            field=models.FileField(null=True, upload_to='Pictures'),
        ),
    ]
