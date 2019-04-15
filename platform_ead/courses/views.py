from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment,Announcement, Lesson
from .forms import ContactCourse, CommentForm
from django.contrib import messages
from .decorators import enrollment_required

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
@enrollment_required
def announcements(request, name):
    course = request.course
    template = 'pages/announcements.html'
    context = {
    'course':course,
    'announcements':course.announcements.all()
    }

    return render(request, template, context)

@login_required
@enrollment_required
def video_classes(request, name):
    course = request.course
    #lesson = get_object_or_404(Lesson, pk=pk, course=course)
    lessons = course.release_lessons()
    if request.user.is_staff:
        lessons = course.lessons.all()
    template = 'pages/video_classes.html'
    context = {
        'course':course,
        'lessons':lessons
    }

    return render(request, template, context)

@login_required
@enrollment_required
def lesson(request, name, pk):
    course = request.course
    lesson = get_object_or_404(Lesson, pk=pk, course=course)
    if not request.user.is_staff and not lesson.is_available():
        messages.error(request,' Essa aula não esta disponivel')
        return redirect('pages/videos_classes.html', name=course.name)
    template = 'pages/video_classes_view.html'
    context = {
    'course':course,
    'lesson':lesson
    }

    return render(request, template, context)

@login_required
@enrollment_required
def comments_view(request, name, pk):
    course = request.course
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
