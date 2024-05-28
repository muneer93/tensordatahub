from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics/')
    career_summary = models.TextField(blank=True, null=True)
    positions = models.ManyToManyField('Positions')
    programming_languages = models.ManyToManyField('Languages')
    databases = models.ManyToManyField('Databases')
    cloud_stack = models.ManyToManyField('CloudStack')
    data_stack = models.ManyToManyField('DataStack')
    analytics_tools = models.ManyToManyField('AnalyticsTools')
    competencies = models.ManyToManyField('Competencies')
    web_frameworks = models.ManyToManyField('WebFramework')
    website = models.URLField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} Profile'

    class Meta:
        verbose_name_plural = 'Profiles'

class Positions(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Position'
    

class Languages(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'

class Databases(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Databases'

class CloudStack(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cloud Stack'


class DataStack(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Data Stack'
    

class AnalyticsTools(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Analytics Tools'

class WebFramework(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Web Frameworks'

class Competencies(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Competencies'

class Experience(models.Model):
    designation = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.TextField(blank=True, null=True)
    achievement = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.designation} - {self.company}"
    
    
    class Meta:
        verbose_name_plural = 'Experience'