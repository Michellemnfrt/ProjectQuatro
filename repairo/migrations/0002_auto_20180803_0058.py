# Generated by Django 2.0.5 on 2018-08-03 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='song',
            new_name='car',
        ),
    ]
