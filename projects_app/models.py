from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

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
        # Check if there's an image and it needs to be resized
        if self.project_photo:
            # Open the image and resize if necessary
            img = Image.open(self.project_photo)
            if img.height > 450 or img.width > 350:
                output_size = (450, 350)
                img.thumbnail(output_size)

                # Save the resized image to a BytesIO object
                img_io = BytesIO()
                img.save(img_io, format=img.format)
                img_content = ContentFile(img_io.getvalue(), self.project_photo.name)

                # Set the image field to the resized image
                self.project_photo.save(self.project_photo.name, img_content, save=False)

        # Call the parent class's save method to save the instance
        super().save(*args, **kwargs)