# Generated by Django 2.0.2 on 2018-06-23 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobsConfig',
            new_name='Job',
        ),
    ]
