from django.contrib.auth import views as auth_views
from django.urls import path, include
from platform_ead.accounts import views

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(template_name='login/login.html'),name='accounts' ),
    path('registrar-se/', views.register ,name='register' ),
]