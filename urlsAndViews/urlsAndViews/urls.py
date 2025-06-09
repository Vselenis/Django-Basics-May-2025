from django.contrib import admin
from django.urls import path, include

from department.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('department/', include("department.urls"))
]
