# Generated by Django 2.1.1 on 2018-10-04 19:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budrys_app', '0005_auto_20181004_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animals',
            name='img_s',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250, null=True), size=8),
        ),
    ]
