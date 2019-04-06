from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from .models import Course

def courses(request):
    courses = Course.objects.all()
    context={
        'courses': courses
    }
    templateName = "pages/courses.html"
    return render(request, templateName, context)

def details(request, slug):
    # course = get_object_or_404(Course, id=id)
    try:
        course = Course.objects.get(slug=slug)
    except Course.DoesNotExist:
        raise Http404("LARGA DE SER BIZNHO ESTE CURSO NÃO  EXISTE")
    context={
        'course':course
    }
    templateName = "pages/details.html"

    return render(request,templateName,context)

