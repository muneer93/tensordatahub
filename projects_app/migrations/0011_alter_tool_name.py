# Generated by Django 4.2.10 on 2024-03-01 00:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects_app", "0010_alter_tool_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tool",
            name="name",
            field=models.CharField(max_length=25),
        ),
    ]
