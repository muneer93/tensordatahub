from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import MyProjects, ProjectList

def home(request):
    project_types = ProjectList.objects.all()
    projects_by_type = {ptype.project_type: MyProjects.objects.filter(project_type=ptype) for ptype in project_types}

    context = {
    'project_types': project_types,
    'projects_by_type': projects_by_type,
    }
    return render(request, 'projects_app/project_home1.html', context)


def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'projects_app/about.html', context)


def project_html_template(request, title):
    project = get_object_or_404(MyProjects, title=title)
    if project.html_file:
        html_content = project.html_file.read().decode('utf-8')
        context = {
            'html_content': html_content,
            'project': project
        }
        return render(request, 'projects_app/project_template.html', context)
    else:

        return render(request, 'not_found.html')
