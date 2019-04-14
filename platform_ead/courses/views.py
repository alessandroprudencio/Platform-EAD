from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from .forms import ContactCourse, CommentForm
from django.contrib import messages

def courses(request):
    courses = Course.objects.all()

    context={
        'courses': courses,
        'form' : ContactCourse()
    }
    templateName = "pages/courses.html"
    return render(request, templateName, context)

def details(request, name):
    # course = get_object_or_404(Course, id=id)
    try:
        course = Course.objects.get(name=name)

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
def announcements(request, name):
    course = get_object_or_404(Course, name=name)

    if not request.user.is_staff:
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        if not enrollment.is_approved():
            messages.error(request,"Erro inscrição está pendente!")
            return redirect('dashboard')

    template = 'pages/announcements.html'
    context = {
    'course':course,
    'announcements':course.announcements.all()
    }

    return render(request, template, context)

@login_required
def comments_view(request, name, pk):
    course = get_object_or_404(Course, name=name)
    if not request.user.is_staff:
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        if not enrollment.is_approved():
            messages.error(request,"Erro inscrição está pendente!")
            return redirect('dashboard')
    form = CommentForm(request.POST or None)
    announcement = get_object_or_404(course.announcements.all(), pk=pk)
    

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        form = CommentForm() 
        messages.success(request, 'Seu comentario foi adicionado!')   

    template = 'pages/comments_view.html'
    context = {
    'course':course,
    'announcement':announcement,
    'form':form
    }

    return render(request, template, context)



@login_required
def enrollment(request, name):
    course = get_object_or_404(Course, name=name)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user,course=course)
    if created:
        # enrollment.active()
        messages.success(request,'Parabéns você foi inscrito com sucesso!')
    else:
        messages.info(request, 'OPS! Você já esta inscrito neste curso.')

    return redirect('dashboard')

@login_required
def undo_enrollment(request, name):
     course = get_object_or_404(Course, name=name)
     enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
     if request.method == 'POST':
        enrollment.delete()
        if enrollment.delete():
            messages.success(request, 'Inscrição cancelada com sucesso!')
        else:
            messages.error(request, 'Não foi possivel desinscrever-se!')

        return redirect('dashboard/dashboard.html')

     template = 'dashboard/dashboard.html'

     context = {
     'enrollment':enrollment,
     'course':course
     }

     return render(request,template, context)
