# Generated by Django 4.2.10 on 2024-05-22 00:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_profile", "0011_rename_languages_profile_programming_languages"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]