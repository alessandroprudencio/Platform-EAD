from platform_ead.forum import views
from django.urls import path, include

urlpatterns = [
    path('',views.ForumView.as_view(), name='forum'),
    path('tag/<tag>/',views.ForumView.as_view(), name='index_tagged'),
    path('duvida/<pk>/', views.ThreadView.as_view(), name="details")
]
