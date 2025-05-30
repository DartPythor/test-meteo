# Generated by Django 4.2 on 2025-05-27 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("weather", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SearchStat",
            fields=[
                (
                    "city",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="weather.citycached",
                    ),
                ),
                ("count", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="SearchHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "session_key",
                    models.CharField(
                        help_text="Сессия пользователя", max_length=124
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="weather.citycached",
                    ),
                ),
            ],
        ),
    ]
