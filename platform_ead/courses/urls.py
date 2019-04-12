from platform_ead.courses import views
from django.urls import path, include

urlpatterns = [
    path('',views.courses, name='courses'),
    path('<slug>/', views.details, name='details'),
    path('inscrever-se/<slug>/', views.enrollment, name='enrollments'),
    path('anuncio/<slug>/', views.announcements, name='announcements'),
    
]
