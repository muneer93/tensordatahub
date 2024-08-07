# Generated by Django 4.2.10 on 2024-07-29 03:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects_app", "0022_alter_dataanalysisproject_html_file_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataanalysisproject",
            name="data_source",
            field=models.URLField(
                blank=True,
                default="https://www.thedatamatrix.ca/",
                max_length=250,
                null=True,
            ),
        ),
    ]
