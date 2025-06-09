from django.contrib import admin

# Register your models here.
from department.models import Department


@admin.register(Department)

class DepartmentAdmin(admin.ModelAdmin):
    pass