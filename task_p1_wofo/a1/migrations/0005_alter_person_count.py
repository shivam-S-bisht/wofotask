# Generated by Django 3.2 on 2021-04-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0004_alter_person_time_when_boolean_field_changes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]