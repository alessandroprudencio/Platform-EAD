from django.contrib import admin
from platform_ead.core import views
from django.urls import path


urlpatterns = [
    path('contato/', views.contact, name="contact"),
    path('', views.home, name="home"),

]