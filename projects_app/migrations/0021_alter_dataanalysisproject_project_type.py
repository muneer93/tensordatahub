# Generated by Django 4.2.10 on 2024-06-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects_app", "0020_remove_dataanalysisproject_app_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataanalysisproject",
            name="project_type",
            field=models.CharField(
                blank=True, default="Data Analysis", max_length=100, null=True
            ),
        ),
    ]
