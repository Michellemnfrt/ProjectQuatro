# Generated by Django 2.0.5 on 2018-08-17 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repairo', '0006_auto_20180816_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='car',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='repairs', to='repairo.Car'),
        ),
    ]
