# Generated by Django 3.0.5 on 2020-08-08 13:37

import os

import django.contrib.postgres.indexes
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("challenge", "0001_initial"),
        ("team", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="solve",
            name="solved_by",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="solves", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="solve",
            name="team",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name="solves", to="team.Team"),
        ),
        migrations.AddField(
            model_name="score",
            name="team",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name="scores", to="team.Team"),
        ),
        migrations.AddField(
            model_name="score",
            name="user",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="scores", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="file",
            name="challenge",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="file_set", to="challenge.Challenge"),
        ),
        migrations.AddField(
            model_name="challenge",
            name="category",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="category_challenges", to="challenge.Category"),
        ),
        migrations.AddField(
            model_name="challenge",
            name="first_blood",
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="first_bloods", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="challenge",
            name="unlocks",
            field=models.ManyToManyField(blank=True, related_name="unlocked_by", to="challenge.Challenge"),
        ),
    ]

    if settings.DATABASES.get("default", {}).get("ENGINE", "").endswith("postgresql"):
        operations.append(
            migrations.AddIndex(
                model_name="solve",
                index=django.contrib.postgres.indexes.BrinIndex(autosummarize=True, fields=["challenge"], name="challenge_s_challen_dd8715_brin"),
            )
        )

    operations.extend(
        [
            migrations.AddConstraint(
                model_name="solve",
                constraint=models.UniqueConstraint(condition=models.Q(("correct", True), ("team__isnull", False)), fields=("team", "challenge"), name="unique_team_challenge_correct"),
            ),
            migrations.AddConstraint(
                model_name="solve",
                constraint=models.UniqueConstraint(condition=models.Q(correct=True), fields=("solved_by", "challenge"), name="unique_member_challenge_correct"),
            ),
        ]
    )
