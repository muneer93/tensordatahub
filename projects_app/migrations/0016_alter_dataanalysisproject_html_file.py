# Generated by Django 4.2.10 on 2024-05-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects_app", "0015_alter_dataanalysisproject_html_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataanalysisproject",
            name="html_file",
            field=models.FileField(
                blank=True,
                default="html_files/default.html",
                null=True,
                upload_to="html_files/",
            ),
        ),
    ]
