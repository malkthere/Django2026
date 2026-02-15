from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the Students Application'
    }
    return render(request, 'students/home.html', context)

def about(request):
    context = {
        'title': 'About Page',
        'description': 'This application is built using Django.'
    }
    return render(request, 'students/about.html', context)

def contactus(request):
    context = {
        'title': 'Contact Page',
        'description': 'developed by Dr. Mazin Alkathiti. E-mail: malkthere@seiyunu.edu.ye'

    }
    return render(request, 'students/contactus.html', context)



def student_detail(request, student_id):
    return HttpResponse(f"Student Profile Page - ID: {student_id}")
