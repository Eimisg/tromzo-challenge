import graphene

from django.utils import timezone
from graphene_django import DjangoObjectType

from .models import Object


class ObjectType(DjangoObjectType):
    class Meta:
        Field = "__all__"
        model = Object


class ObjectQuery(graphene.ObjectType):
    get_object = graphene.Field(ObjectType, object_id=graphene.Int())

    @staticmethod
    def resolve_get_object(self, info, **kwargs):
        obj = Object.objects.filter(taken_at__isnull=True).first()
        if not obj:
            return None
        obj.taken_at = timezone.now()
        obj.save()
        return obj


class ObjectInput(graphene.InputObjectType):
    id = graphene.ID()


class FreeObjectMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    object = graphene.Field(ObjectType)

    @classmethod
    def mutate(cls, root, info, id):
        obj = Object.objects.get(pk=id)
        if obj:
            obj.taken_at = None
            obj.save()
            return FreeObjectMutation(object=obj)
        return FreeObjectMutation(object=None)


class ObjectMutation(graphene.ObjectType):
    free_object = FreeObjectMutation.Field()
