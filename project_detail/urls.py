from django.urls import path
from .views import project_create, project_index, project_view, task_create

urlpatterns = [
    path("", project_index),
    path("create", project_create),
    path("view/<int:id>", project_view, name="project-view"),
    ##
    path("task/create/<int:project_id>", task_create, name="task-create")
]
