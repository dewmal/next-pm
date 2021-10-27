from graphene_django import DjangoObjectType

from .models import Project, Task, Step, Tag


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class StepType(DjangoObjectType):
    class Meta:
        model = Step
