from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('test/', views.test_view, name='test'), 
    path('next-question/', views.next_question, name='next_question'),
    path('prev-question/', views.prev_question, name='prev_question'),
    path('completion/', views.completion_view, name='completion'),
]
