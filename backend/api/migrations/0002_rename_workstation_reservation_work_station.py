# Generated by Django 4.2.3 on 2023-08-02 13:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="workStation",
            new_name="work_station",
        ),
    ]
