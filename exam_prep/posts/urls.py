from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    #path('posts/create/', views.post_create, name='post_create'),
    #path('posts/<int:post_id>/details/', views.post_details, name='post_details'),
    #path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    #path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
]