from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages

from .models import Course, Enrollment

def enrollment_required(view_func):
    def _wrapper(request, *args, **kwargs):
        name = kwargs['name']
        course = get_object_or_404(Course, name=name)
        has_permission = request.user.is_staff
        if not has_permission:
            try:
                enrollment = Enrollment.objects.get(
                    user=request.user, course = course
                )
            except Enrollment.DoesNotExist:
                message = 'Desculpe, mas você não tem permissão para acessar esta pagina'
            else:
                if enrollment.is_approved():
                    has_permission = True
                else:
                    message = 'A sua inscrição no curso ainda esta pendente'

        if not has_permission:
            message.erro(request, message)
            redirect('dashboard/dashboard.html')
        
        request.course = course 
        return view_func(request, *args, **kwargs)
    return _wrapper