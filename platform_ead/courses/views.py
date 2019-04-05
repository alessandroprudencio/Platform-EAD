from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

def courses(request):
    courses = Course.objects.all()
    context={
        'courses': courses
    }
    templateName = "pages/courses.html"
    return render(request, templateName, context)

