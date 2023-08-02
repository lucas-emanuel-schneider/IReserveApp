# Generated by Django 4.2.3 on 2023-08-02 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated"),
                ),
                ("address", models.CharField(max_length=255, verbose_name="address")),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email"
                    ),
                ),
                ("mobile", models.CharField(max_length=255, verbose_name="phone")),
                (
                    "username",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="username"
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WorkStation",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated"),
                ),
                (
                    "station",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="station"
                    ),
                ),
                ("available", models.BooleanField()),
            ],
            options={
                "verbose_name": "Station",
                "verbose_name_plural": "Stations",
            },
        ),
        migrations.CreateModel(
            name="Reservation",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated"),
                ),
                ("reservation_date", models.DateField(verbose_name="reservation_date")),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "workStation_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workStation_id",
                        to="api.workstation",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reservation",
                "verbose_name_plural": "Reservations",
            },
        ),
    ]
