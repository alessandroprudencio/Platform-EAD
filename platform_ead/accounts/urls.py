from django.contrib.auth import views as auth_views
from django.urls import path, include
from platform_ead.accounts import views

urlpatterns = [
    path('', views.dashboard ,name='dashboard' ),
    path('entrar/', auth_views.LoginView.as_view(template_name='login/login.html'),name='accounts' ),
    path('registrar-se/', views.register ,name='register' ),
    path('sair', auth_views.LogoutView.as_view(template_name='login/login.html', next_page='/'),name="logout"),
    path('editar',views.edit  ,name="edit"),
    path('recuperar_senha',views.password_reset  ,name="password_reset"),
    path('nova_senha/<key>/',views.password_reset_confirm  ,name="password_reset_confirm"),
    
]