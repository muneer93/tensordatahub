from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

PROJECT_TYPE = [
    ('Data Analysis', 'Data Analysis'),
    ('Data Engineering', 'Data Engineering'),
    ('Machine Learning', 'Machine Learning')
]

class Tool(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class DataAnalysisProject(models.Model):
    title = models.CharField(max_length=100, unique=True)
    project_type = models.CharField(max_length=35, choices=PROJECT_TYPE, default='Data Analysis')
    tools = models.ManyToManyField('Tool')
    description = models.CharField(max_length=250, blank=True, null=True)
    published_date = models.DateField(default=timezone.now)
    analyst = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    problem_statement = models.TextField(blank=True, null=True)
    insights = models.TextField(blank=True, null=True)
    html_file = models.FileField(upload_to='html_files/', default='default.html', blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    project_photo = models.ImageField(upload_to='project_pics/', blank=True, null=True)
    data_source = models.URLField(max_length=250, default='local.io', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Data Analysis Projects"

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if self.project_photo:
            super().save(*args, **kwargs)

            img = Image.open(self.project_photo.path)

            if img.height > 450 or img.width > 350:
                output_size = (450, 350)
                img.thumbnail(output_size)
                img.save(self.project_photo.path)
        else:
            super().save(*args, **kwargs)



