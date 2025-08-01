from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('events/', include('events.urls')),
    path('organizer/', include('organizers.urls')),
]