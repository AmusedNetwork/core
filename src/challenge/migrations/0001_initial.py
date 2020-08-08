# Generated by Django 3.0.5 on 2020-08-08 13:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36, unique=True)),
                ('display_order', models.IntegerField()),
                ('contained_type', models.CharField(max_length=36)),
                ('description', models.TextField()),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('release_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36, unique=True)),
                ('description', models.TextField()),
                ('challenge_type', models.CharField(max_length=64)),
                ('challenge_metadata', django.contrib.postgres.fields.jsonb.JSONField()),
                ('flag_type', models.CharField(default='plaintext', max_length=64)),
                ('flag_metadata', django.contrib.postgres.fields.jsonb.JSONField()),
                ('author', models.CharField(max_length=36)),
                ('auto_unlock', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('score', models.IntegerField()),
                ('points_type', models.CharField(default='basic', max_length=64)),
                ('release_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.URLField()),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=64)),
                ('points', models.IntegerField()),
                ('penalty', models.IntegerField(default=0)),
                ('leaderboard', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Solve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_blood', models.BooleanField(default=False)),
                ('correct', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('flag', models.TextField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solves', to='challenge.Challenge')),
                ('score', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solve', to='challenge.Score')),
            ],
        ),
    ]