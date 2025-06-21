from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import AuthorCreateForm

def author_create(request):
    if request.method == 'POST':
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to dashboard after success
            return redirect('dashboard')
    else:
        form = AuthorCreateForm()
    # Pass nav logic to template: no profile yet!
    context = {'form': form, 'has_author_profile': False}
    return render(request, 'create-author.html', context)