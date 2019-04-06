from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(template_name='registration/login.html'),name='accounts' ),
]