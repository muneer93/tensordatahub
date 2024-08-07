# Generated by Django 4.2.10 on 2024-07-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("my_profile", "0016_remove_profile_links_delete_profilelink"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileLink",
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
                ("name", models.CharField(max_length=50)),
                ("url", models.URLField()),
            ],
            options={
                "verbose_name_plural": "Profile Links",
            },
        ),
    ]
