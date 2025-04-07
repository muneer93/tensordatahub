# Generated by Django 4.2.10 on 2025-04-07 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0029_alter_myprojects_project_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprojects',
            name='html_file',
            field=models.FileField(blank=True, default='html_files/default.html', max_length=250, null=True, upload_to='html_files/'),
        ),
        migrations.AlterField(
            model_name='myprojects',
            name='project_photo',
            field=models.ImageField(blank=True, default='project_pics/default.jpeg', max_length=250, null=True, upload_to='project_pics/'),
        ),
    ]
