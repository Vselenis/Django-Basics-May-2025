from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.urls import reverse

from department.models import Department


def index(request):
    return HttpResponse("<h1>Department Home Page</h1>")

def int_param_view(request, pk: int):
    return HttpResponse(f"<h1>Department index: {pk}</h1>")

def string_param_view(request, name):
    return HttpResponse(f"<h1>Department index: {name}</h1>")

def slug_param_view(request, slug):
    department = Department.objects.filer(slug=slug).first()
    return render(request, "slug_template.html", {"department": department})

def file_path_param_view(request, path_to_file):
    return HttpResponse(f"<h1>The path is located at {path_to_file}:</h1>")

def uuid_param_view(request, id):
    return HttpResponse(f"<h1>The unique id is: {id}:</h1>")

def regex_view(request, archive_year:int):
    return HttpResponse(f"<h1>The year is: {archive_year}:</h1>")

def contacts_view(request):
    print(reverse('contacts'))
    return HttpResponse(f"<h1>We are departments</h1>")

def about_view(request):
    return redirect("contacts", permanent=True)
