from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.organizer_create, name='organizer_create'),
    path('details/', views.organizer_details, name='organizer_details'),
    path('edit/', views.organizer_edit, name='organizer_edit'),
    path('delete/', views.organizer_delete, name='organizer_delete'),
]
