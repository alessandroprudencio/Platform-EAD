from platform_ead.courses import views
from django.urls import path, include

urlpatterns = [
    path('',views.courses, name='courses'),
    path('<name>/', views.details, name='details'),
    path('inscrever-se/<name>/', views.enrollment, name='enrollments'),
    path('anuncio/<name>/', views.announcements, name='announcements'),
    path('comentarios/<name>/<pk>/', views.comments_view, name='comments_view'),
    path('cancelar-inscricao/<name>/',views.undo_enrollment, name="undo_enrollment"),
]
