from views import index, dashboard
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
]