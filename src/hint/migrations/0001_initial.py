# Generated by Django 3.0.5 on 2020-08-08 13:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('text', models.TextField()),
                ('penalty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HintUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hints_used', to='challenge.Challenge')),
                ('hint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uses', to='hint.Hint')),
            ],
        ),
    ]
