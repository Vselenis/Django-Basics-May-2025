from django.shortcuts import render

def index(request):
    # You can set has_author_profile to False for now, or your actual logic
    context = {'has_author_profile': False}
    return render(request, 'index.html', context)