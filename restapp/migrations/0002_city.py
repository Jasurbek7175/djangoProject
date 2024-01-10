# Generated by Django 4.2.7 on 2024-01-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=255)),
                ("area", models.IntegerField()),
                ("population", models.IntegerField()),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
        ),
    ]