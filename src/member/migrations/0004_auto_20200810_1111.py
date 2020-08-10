# Generated by Django 3.0.5 on 2020-08-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20200808_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='totp_secret',
        ),
        migrations.RemoveField(
            model_name='member',
            name='totp_status',
        ),
        migrations.AddField(
            model_name='member',
            name='state_actor',
            field=models.BooleanField(default=False),
        ),
    ]