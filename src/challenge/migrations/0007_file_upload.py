# Generated by Django 3.1.4 on 2020-12-23 16:22

from django.db import migrations, models

import challenge.models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='upload',
            field=models.FileField(default='', upload_to=challenge.models.get_file_name),
            preserve_default=False,
        ),
    ]
