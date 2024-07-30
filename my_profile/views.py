from django.shortcuts import render
from .models import Profile, Experience

def profile(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all().order_by('-start_date')  # Sort experiences by start_date descending
    languages = profile.programming_languages.all()
    databases = profile.databases.all()
    data_stack = profile.data_stack.all()
    cloud_stack = profile.cloud_stack.all()
    frameworks = profile.web_frameworks.all()
    competencies = profile.competencies.all()
    interests = profile.interests.all()
    context = {
        'profile': profile,
        'experiences': experiences,
        'databases': databases,
        'languages': languages,
        'data_stack': data_stack,
        'cloud_stack': cloud_stack,
        'frameworks': frameworks,
        'competencies': competencies,
        'interests': interests
    }
    return render(request, 'my_profile/profile.html', context)
