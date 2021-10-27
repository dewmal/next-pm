import graphene

from project_detail.models import Project, Task
from project_detail.mutations import UpdateTask
from project_detail.types import ProjectType, TaskType


class Query(graphene.ObjectType):
    projects = graphene.List(ProjectType)
    project = graphene.Field(ProjectType, project_id=graphene.Int())
    tasks = graphene.List(TaskType, project_id=graphene.Int())

    def resolve_projects(self, info, **kwargs):
        return Project.objects.all().order_by("-start_date")

    def resolve_project(self, info, project_id):
        return Project.objects.get(id=project_id)


class Mutation(graphene.ObjectType):
    update_task = UpdateTask.Field()


schema = graphene.Schema(query=Query, auto_camelcase=True, mutation=Mutation)
