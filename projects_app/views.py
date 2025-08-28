from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MyProjects, ProjectList

def home(request):
    project_types = ProjectList.objects.all()
    projects_by_type = {ptype.project_type: MyProjects.objects.filter(project_type=ptype) for ptype in project_types}

    context = {
    'project_types': project_types,
    'projects_by_type': projects_by_type,
    }
    return render(request, 'projects_app/project_home.html', context)


def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'projects_app/about.html', context)


def project_html_template(request, title):
    # This correctly fetches the project object from the database.
    # The get_object_or_404 function will return a 404 error if the project is not found.
    project = get_object_or_404(MyProjects, title=title)

    # We create a context dictionary and pass the entire project object to the template.
    context = {
        'project': project,
    }

    # Now, we render a new, dynamic template called 'project_detail.html'
    # The template will use Django's template language to display the project data.
    return render(request, 'projects_app/project_detail.html', context)