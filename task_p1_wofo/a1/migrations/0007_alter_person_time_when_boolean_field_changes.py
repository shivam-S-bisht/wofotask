# Generated by Django 3.2 on 2021-04-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0006_alter_person_time_when_boolean_field_changes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='time_when_boolean_field_changes',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
