import graphene

from project_detail.models import Project, Task
from project_detail.mutations import UpdateTask
from project_detail.types import ProjectType, TaskType, TaskStatusType


class ProjectQuery(graphene.ObjectType):
    task_status = graphene.List(TaskStatusType)
    projects = graphene.List(ProjectType)
    project = graphene.Field(ProjectType, project_id=graphene.Int())
    tasks = graphene.List(TaskType, project_id=graphene.Int())

    def resolve_projects(self, info, **kwargs):
        return Project.objects.all().order_by("-start_date")

    def resolve_project(self, info, project_id):
        return Project.objects.get(id=project_id)

    def resolve_task_status(self, info):
        return map(lambda st: {"name": st[1], "value": st[0]}, Task.STEP_STATUSES)


class ProjectMutation(graphene.ObjectType):
    update_task = UpdateTask.Field()
