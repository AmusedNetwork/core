# Generated by Django 3.0.5 on 2020-08-08 15:49

import django.contrib.postgres.fields.citext
from django.db import migrations

import backend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=django.contrib.postgres.fields.citext.CICharField(max_length=36, unique=True, validators=[backend.validators.printable_name]),
        ),
    ]
