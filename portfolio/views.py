from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
import random

def HomePage(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/HomePage.html', {'projects': projects})


