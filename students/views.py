from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'students/home.html')

def student_detail(request, student_id):
    return HttpResponse(f"Student Profile Page - ID: {student_id}")
