# Generated by Django 2.1.1 on 2018-10-18 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualiser', '0010_auto_20181018_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='visualiser/management/commands/documents/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
