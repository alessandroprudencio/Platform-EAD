from django.template import Library

register = Library()

from platform_ead.courses.models import Enrollment

@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context  



@register.inclusion_tag('courses/templatetags/my_courses_price.html')
def my_courses_price(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context  

@register.inclusion_tag('courses/templatetags/my_courses_date_buy.html')
def my_courses_date_buy(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context  


@register.inclusion_tag('courses/templatetags/my_personal_data.html')
def my_personal_data(user):
    context = {
       'user':user
    }
    return context  


