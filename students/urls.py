from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='students_home'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
]
