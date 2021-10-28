from datetime import datetime

import graphene

from .models import Task
from .project_service import ProjectService
from .types import TaskType


class UpdateTask(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        pull_requests = graphene.String()
        description = graphene.String()
        end_time = graphene.String()
        status = graphene.String()

    ok = graphene.Boolean()
    task = graphene.Field(lambda: TaskType)

    def mutate(root, info, id, pull_requests=None, description=None, end_time=None, status=None):
        print(id, pull_requests, description, end_time, status)
        task = Task.objects.get(id=id)
        task.pull_requests = pull_requests if pull_requests is not None else task.pull_requests
        task.description = description if description is not None else task.description
        task.end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        task.status = status
        task = ProjectService.close_task(task)
        ok = True
        return UpdateTask(task=task, ok=ok)
