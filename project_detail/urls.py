from django.urls import path
from .views import project_create, project_index, project_view, \
    task_create, task_view, task_step_create, step_view

urlpatterns = [
    path("", project_index),
    path("create", project_create),
    path("view/<int:id>", project_view, name="project-view"),
    ##
    path("task/create/<int:project_id>", task_create, name="task-create"),
    path("task/view/<int:id>", task_view, name="task-view"),
    path("task/step/create/<int:task_id>", task_step_create, name="task-step-create"),
    path("task/step/view/<int:step_id>", step_view, name="step-view"),

]
