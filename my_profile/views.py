from django.shortcuts import render
from .models import Profile, Experience


def profile(request):
    profile = Profile.objects.first()
    experience = Experience.objects.all()
    languages = profile.programming_languages.all()
    databases = profile.databases.all()
    datastack = profile.data_stack.all()
    cloudstack = profile.cloud_stack.all()
    framework = profile.web_frameworks.all()
    competencies = profile.competencies.all()
    context = {
        'profile': profile,
        'experiences': experience,
        'databases': databases,
        'languages': languages,
        'data_stack': datastack,
        'cloud_stack': cloudstack,
        'frameworks': framework,
        'competencies': competencies
    }
    return render(request, 'my_profile/index.html', context)