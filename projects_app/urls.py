from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='project_home'),
    path('about/', views.about, name='projects-about'),
    path('project/<str:title>/', views.project_html_template, name='project_html_template'),
    path('ckeditor5/', include('django_ckeditor_5.urls')), 
]