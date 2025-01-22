# Generated by Django 5.1.5 on 2025-01-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinelink_api", "0003_alter_movie_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="activity",
            options={"verbose_name": "Activity", "verbose_name_plural": "Activities"},
        ),
        migrations.AlterModelOptions(
            name="friend",
            options={"verbose_name": "Friend", "verbose_name_plural": "Friends"},
        ),
        migrations.AlterModelOptions(
            name="listmovie",
            options={
                "verbose_name": "List Movie",
                "verbose_name_plural": "List Movies",
            },
        ),
        migrations.AlterModelOptions(
            name="rating",
            options={"verbose_name": "Rating", "verbose_name_plural": "Ratings"},
        ),
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
