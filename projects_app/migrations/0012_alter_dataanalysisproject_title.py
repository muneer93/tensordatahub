# Generated by Django 4.2.10 on 2024-03-01 22:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects_app", "0011_alter_tool_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataanalysisproject",
            name="title",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
