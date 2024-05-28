from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects-home'),
    path('about/', views.about, name='projects-about'),
    path('project/<str:title>/', views.project_html_template, name='project_html_template')
]