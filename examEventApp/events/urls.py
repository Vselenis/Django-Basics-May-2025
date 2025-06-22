from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_list, name='events_list'),
    path('create/', views.event_create, name='event_create'),
    path('<int:event_pk>/details/', views.event_details, name='event_details'),
    path('<int:event_pk>/edit/', views.event_edit, name='event_edit'),
    path('<int:event_pk>/delete/', views.event_delete, name='event_delete'),
]