from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot_view'),
    path('get_response/', views.get_gemini_response, name='get_gemini_response'),
]