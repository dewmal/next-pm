from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import ProjectForm, TaskForm
from .models import Project


@require_http_methods(["GET", "POST"])
def task_create(request, project_id):
    project = Project.objects.get(id=project_id)
    form = TaskForm(prefix="task")
    errors = None
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES, prefix="task")
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            errors = form.errors

    return render(request, "task/create.html", context={"project": project, "form": form, "errors": errors})


@require_http_methods(["GET"])
def project_index(request):
    all = Project.objects.all()
    return render(request, "project/all.html", context={"projects": all})


def project_view(request, id):
    project = Project.objects.get(id=id)
    return render(request, "project/view.html", context={"project": project})


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
