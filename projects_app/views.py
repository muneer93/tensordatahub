from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import DataAnalysisProject

def home(request):
    project = DataAnalysisProject.objects.all()
    context = {
        'project': project
    }
    return render(request, 'projects_app/project_home.html', context)

def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'projects_app/about.html', context)


def project_html_template(request, title):
    # Retrieve the DataAnalysisProject object using the title
    project = get_object_or_404(DataAnalysisProject, title=title)
    # Check if the HTML file path is not empty
    if project.html_file:
        html_content = project.html_file.read().decode('utf-8')  # Read HTML file content
        context = {
            'html_content': html_content,
            'project': project
        }
        return render(request, 'projects_app/project_template.html', context)
    else:

        return render(request, 'not_found.html')
