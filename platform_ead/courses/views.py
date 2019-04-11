from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Course, Enrollment
from .forms import ContactCourse



def courses(request):
    courses = Course.objects.all()

    context={
        'courses': courses,
        'form' : ContactCourse()
    }
    templateName = "pages/courses.html"
    return render(request, templateName, context)

def details(request, slug):
    # course = get_object_or_404(Course, id=id)
    try:
        course = Course.objects.get(slug=slug)

        context = {}

        if request.method == 'POST':
            form  = ContactCourse(request.POST)
            if form.is_valid():
                context['is_valid'] = True
                form.send_mail(course)  
                form = ContactCourse()

        else:
            form = ContactCourse(),
    except Course.DoesNotExist:
        raise Http404("LARGA DE SER BIZNHO ESTE CURSO NÃO  EXISTE")
    context['form'] = form
    context['course'] = course

    templateName = "pages/details.html"

    return render(request,templateName,context)

@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug) 
    enrollment,created = Enrollment.objects.get_or_create(
        user = request.user,
        course = course
        )
    if created:
      messages.success(request, 'Inscrito com Sucesso!.')
    else:
      messages.info(request, 'Infelizmente você já esta inscrito neste curso')


    return redirect('dashboard')