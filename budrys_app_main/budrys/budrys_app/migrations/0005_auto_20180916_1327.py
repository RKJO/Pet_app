# Generated by Django 2.1.1 on 2018-09-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budrys_app', '0004_auto_20180914_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animals',
            name='evidence_number',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animals',
            name='img_main',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animals',
            name='img_main_alt',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animals',
            name='img_s',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animals',
            name='location',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='animals',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='animals',
            name='race',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='animals',
            name='sex',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='animals',
            name='species',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='animals',
            name='sterilized_castrated',
            field=models.CharField(max_length=1000),
        ),
    ]
