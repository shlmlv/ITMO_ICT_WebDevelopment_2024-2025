# Generated by Django 5.1.5 on 2025-01-19 05:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinelink_api", "0006_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="avatar_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="username",
            field=models.CharField(default="", max_length=150),
            preserve_default=False,
        ),
    ]
