# Generated by Django 2.0.5 on 2018-08-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairo', '0005_auto_20180814_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='car',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]