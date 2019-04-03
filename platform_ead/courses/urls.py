from django.contrib import admin
from pĺatform_ead.courses import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='courses')
]
