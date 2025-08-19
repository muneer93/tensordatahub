from django.contrib import admin
from .models import (
    Profile,
    ProfileLink,
    Positions,
    Languages,
    Databases,
    CloudStack,
    DataStack,
    AnalyticsTools,
    WebFramework,
    Competencies,
    Interests,
    Experience,
    SIEM,
    VulnerabilityManagement,
    IAM,
    SecurityFrameworks,
    NetworkAnalysis,
    GeneralCybersecurity
)

# Custom Admin for the Profile model to handle many-to-many fields
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'city', 
        'country', 
        'website',
    )
    search_fields = (
        'user__username', 
        'user__first_name', 
        'user__last_name', 
        'city', 
        'country',
    )
    filter_horizontal = (
        'positions', 
        'programming_languages', 
        'databases', 
        'cloud_stack', 
        'data_stack', 
        'analytics_tools', 
        'competencies', 
        'web_frameworks', 
        'interests',
        'siem_tools',
        'vulnerability_management',
        'iam_skills',
        'security_frameworks',
        'network_analysis',
        'general_cybersecurity',
    )


# Custom Admin for Models with a single 'name' field
class NameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register your models here
admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileLink)
admin.site.register(Positions, NameAdmin)
admin.site.register(Languages, NameAdmin)
admin.site.register(Databases, NameAdmin)
admin.site.register(CloudStack, NameAdmin)
admin.site.register(DataStack, NameAdmin)
admin.site.register(AnalyticsTools, NameAdmin)
admin.site.register(WebFramework, NameAdmin)
admin.site.register(Competencies, NameAdmin)
admin.site.register(Interests, NameAdmin)
admin.site.register(Experience)
admin.site.register(SIEM, NameAdmin)
admin.site.register(VulnerabilityManagement, NameAdmin)
admin.site.register(IAM, NameAdmin)
admin.site.register(SecurityFrameworks, NameAdmin)
admin.site.register(NetworkAnalysis, NameAdmin)
admin.site.register(GeneralCybersecurity, NameAdmin)
