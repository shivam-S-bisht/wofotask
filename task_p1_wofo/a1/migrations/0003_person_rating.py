# Generated by Django 3.2 on 2021-04-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0002_auto_20210408_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
