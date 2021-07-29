import graphene

from apps.object.schema import ObjectQuery, ObjectMutation


class Query(ObjectQuery):
    pass


class Mutation(ObjectMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
