from platform_ead.courses import views
from django.urls import path, include

urlpatterns = [
    path('',views.courses, name='courses'),
    path('<id>/', views.details, name='details')
]
