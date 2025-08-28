from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django_ckeditor_5.fields import CKEditor5Field


class Tool(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class ProjectList(models.Model):
    project_type = models.CharField(max_length=35, blank=True, null=True, unique=True)

    def __str__(self):
        return self.project_type


class MyProjects(models.Model):
    project_type = models.ForeignKey(ProjectList, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, unique=True)
    tools = models.ManyToManyField('Tool')
    description = models.CharField(max_length=250, blank=True, null=True)
    published_date = models.DateField(default=timezone.now)
    analyst = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    problem_statement = models.TextField(blank=True, null=True)
    insights = models.TextField(blank=True, null=True)
    html_file = models.FileField(upload_to='html_files/', default='html_files/default.html', blank=True, null=True, max_length=250)
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True, null=True, max_length=250)
    project_photo = models.ImageField(upload_to='project_pics/', default='project_pics/default.jpeg', blank=True, null=True, max_length=250)
    data_source = models.URLField(max_length=250, default='https://www.thedatamatrix.ca/', blank=True, null=True)

    # New field to store rich text content with images, etc.
    content = CKEditor5Field('content', config_name='default', null=True)

    class Meta:
        verbose_name_plural = "My Projects"

    def __str__(self):
        return self.title

    def project_title(self):
        return self.title

    # The corrected method is here. It was the commented out line.
    def get_project_type(self):
        if self.project_type:
            return self.project_type.project_type
        return None # Return None or a default value if the foreign key is not set.

    def save(self, *args, **kwargs):
        if self.project_photo:
            img = Image.open(self.project_photo)
            
            if img.height > 450 or img.width > 350:
                output_size = (450, 350)
                img.thumbnail(output_size)
                img_io = BytesIO()
                img.save(img_io, format=img.format)
                img_content = ContentFile(img_io.getvalue(), self.project_photo.name)
                self.project_photo.save(self.project_photo.name, img_content, save=False)
        super().save(*args, **kwargs)
