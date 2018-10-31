# Generated by Django 2.1.1 on 2018-10-22 15:33

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('species', models.CharField(max_length=64, null=True)),
                ('race', models.CharField(max_length=64, null=True)),
                ('sex', models.CharField(max_length=64, null=True)),
                ('age', models.IntegerField(null=True)),
                ('weight', models.CharField(max_length=64, null=True)),
                ('sterilized_castrated', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='img/None/no-img.jpg', upload_to='img/')),
                ('img_main', models.CharField(max_length=240, null=True)),
                ('img_main_alt', models.CharField(max_length=240, null=True)),
                ('img_s', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250, null=True), null=True, size=8)),
                ('url', models.URLField()),
                ('evidence_number', models.CharField(max_length=120, null=True)),
                ('admission_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=120, null=True)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=120)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='animals',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budrys_app.Location'),
        ),
    ]
