from django.shortcuts import render
from .models import (
    Profile,
    Experience,
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
    SIEM,
    VulnerabilityManagement,
    IAM,
    SecurityFrameworks,
    NetworkAnalysis,
    GeneralCybersecurity
)

def profile(request):
    """
    Renders the profile index page with all relevant data.
    """
    profile = Profile.objects.first()
    experiences = Experience.objects.order_by('-start_date')
    profile_links = ProfileLink.objects.all()

    programming_languages = profile.programming_languages.all() if profile else []
    databases = profile.databases.all() if profile else []
    cloud_stack = profile.cloud_stack.all() if profile else []
    data_stack = profile.data_stack.all() if profile else []
    analytics_tools = profile.analytics_tools.all() if profile else []
    competencies = profile.competencies.all() if profile else []
    web_frameworks = profile.web_frameworks.all() if profile else []
    interests = Interests.objects.all()
    positions = profile.positions.all() if profile else []

    siem_tools = SIEM.objects.all() if profile else []
    vulnerability_management = VulnerabilityManagement.objects.all() if profile else []
    iam_skills = IAM.objects.all() if profile else []
    security_frameworks = SecurityFrameworks.objects.all() if profile else []
    network_analysis = NetworkAnalysis.objects.all() if profile else []
    general_cybersecurity = GeneralCybersecurity.objects.all()

    context = {
        'profile': profile,
        'experiences': experiences,
        'profile_links': profile_links,
        'positions': positions,
        'programming_languages': programming_languages,
        'databases': databases,
        'cloud_stack': cloud_stack,
        'data_stack': data_stack,
        'analytics_tools': analytics_tools,
        'competencies': competencies,
        'web_frameworks': web_frameworks,
        'interests': interests,
        'siem_tools': siem_tools,
        'vulnerability_management': vulnerability_management,
        'iam_skills': iam_skills,
        'security_frameworks': security_frameworks,
        'network_analysis': network_analysis,
        'general_cybersecurity': general_cybersecurity,
    }
    return render(request, 'my_profile/index.html', context)
