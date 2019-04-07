# Generated by Django 2.1.1 on 2018-10-18 11:18

import django.core.validators
from django.db import migrations, models
import visualiser.validators


class Migration(migrations.Migration):

    dependencies = [
        ('visualiser', '0011_auto_20181018_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='visualiser/management/commands/documents/', validators=[visualiser.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='document',
            name='topics',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
