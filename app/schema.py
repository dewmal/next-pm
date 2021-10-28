import graphene

from project_detail.schema import ProjectMutation, ProjectQuery


class RootQuery(ProjectQuery, graphene.ObjectType):
    pass


class RootMutation(ProjectMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery, auto_camelcase=True, mutation=RootMutation)
