from django.db import models
from django.contrib.auth.models import User

# This is the main Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics/')
    career_summary = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)

    # Many-to-Many relationships for skills and interests
    positions = models.ManyToManyField('Positions', blank=True)
    programming_languages = models.ManyToManyField('Languages', blank=True)
    databases = models.ManyToManyField('Databases', blank=True)
    cloud_stack = models.ManyToManyField('CloudStack', blank=True)
    data_stack = models.ManyToManyField('DataStack', blank=True)
    analytics_tools = models.ManyToManyField('AnalyticsTools', blank=True)
    competencies = models.ManyToManyField('Competencies', blank=True)
    web_frameworks = models.ManyToManyField('WebFramework', blank=True)
    interests = models.ManyToManyField('Interests', blank=True)
    
    # --- IMPORTANT FIXES START HERE ---
    # These are the missing Many-to-Many relationships for cybersecurity skills
    siem_tools = models.ManyToManyField('SIEM', blank=True)
    vulnerability_management = models.ManyToManyField('VulnerabilityManagement', blank=True)
    iam_skills = models.ManyToManyField('IAM', blank=True)
    security_frameworks = models.ManyToManyField('SecurityFrameworks', blank=True)
    network_analysis = models.ManyToManyField('NetworkAnalysis', blank=True)
    general_cybersecurity = models.ManyToManyField('GeneralCybersecurity', blank=True)
    # --- IMPORTANT FIXES END HERE ---

    def __str__(self) -> str:
        return f'{self.user.first_name} Profile'

    class Meta:
        verbose_name_plural = 'Profiles'


class ProfileLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_links')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Profile Links'


# Experience model (not related to profile directly, as per your original query)
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


# Models for skills (Data and Web)
class Positions(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Positions'

class Languages(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'

class Databases(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Databases'

class CloudStack(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cloud Stack'

class DataStack(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Data Stack'
    
class AnalyticsTools(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Analytics Tools'

class WebFramework(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Web Frameworks'

class Competencies(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Competencies'

class Interests(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Interests'

# --- IMPORTANT FIXES START HERE ---
# These are the missing cybersecurity skill models
class SIEM(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'SIEM Tools'

class VulnerabilityManagement(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Vulnerability Management'

class IAM(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'IAM Skills'

class SecurityFrameworks(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Security Frameworks'

class NetworkAnalysis(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Network Analysis'

class GeneralCybersecurity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'General Cybersecurity'
# --- IMPORTANT FIXES END HERE ---
