from django.template import Library

register = Library()

from platform_ead.courses.models import Enrollment

@register.inclusion_tag('templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments':enrollments
    }

    return context

@register.simple_tag 
def load_my_courses(user):
    return Enrollment.objects.filter(user=user)
    