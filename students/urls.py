from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='students-home'),
    path('about/', views.about, name='students-about'),
    path('contactus/', views.contactus, name='contactus'),

    path('<int:student_id>/', views.student_detail, name='student_detail'),
]
