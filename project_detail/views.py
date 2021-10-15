from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import ProjectForm


# Create your views here.
@require_http_methods(["GET", "POST"])
def project_create(request):
    form = ProjectForm(prefix="proj")
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, prefix="proj")
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, "project/create.html", {'form': form})
