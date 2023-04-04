from django.shortcuts import render
from .models import Project


def HomePage(request):
    projects = Project.objects.order_by('project_number')
    return render(request, 'portfolio/HomePage.html', {'projects': projects})


