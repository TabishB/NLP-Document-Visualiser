# Generated by Django 2.1.1 on 2018-10-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualiser', '0008_auto_20181018_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='topics',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
    ]
