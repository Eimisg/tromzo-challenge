from django.utils import timezone
from graphene_django.utils.testing import GraphQLTestCase
from model_bakery.baker import make


class GetObjectQueryTestCase(GraphQLTestCase):

    def setUp(self):
        super().setUp()
        self.object = make("Object")

    def test_get_object_query(self):
        response = self.query(
            """
            query {
                getObject {
                    id,
                    takenAt
                }
            }
            """,
        )
        self.assertResponseNoErrors(response)
        content = response.json()
        self.assertEqual(content["data"]["getObject"]["id"], str(self.object.id))
        self.assertIsNotNone(content["data"]["getObject"]["takenAt"])

    def test_get_object_query_first_object_taken(self):
        self.object.taken_at = timezone.now()
        self.object.save()
        response = self.query(
            """
            query {
                getObject {
                    id,
                    takenAt
                }
            }
            """,
        )
        self.assertResponseNoErrors(response)
        content = response.json()
        self.assertIsNone(content["data"]["getObject"])


class FreeObjectMutationTestCase(GraphQLTestCase):

    def setUp(self):
        super().setUp()
        self.object = make("Object")

    def test_free_object_mutation(self):
        self.object.taken_at = timezone.now()
        self.object.save()
        response = self.query(
            """
            mutation Mutation($id: ID!) {
                freeObject(id: $id) {
                    object {
                        id,
                        takenAt
                    }
                }
            }
            """,
            variables={"id": self.object.id}
        )
        self.assertResponseNoErrors(response)
        obj = response.json()["data"]["freeObject"]["object"]
        self.assertEqual(obj["id"], str(self.object.id))
        self.assertIsNone(obj["takenAt"])

    def test_free_object_mutation_not_found(self):
        self.object.taken_at = timezone.now()
        self.object.save()
        response = self.query(
            """
            mutation Mutation($id: ID!) {
                freeObject(id: $id) {
                    object {
                        id,
                        takenAt
                    }
                }
            }
            """,
            variables={"id": 99}
        )
        self.assertResponseHasErrors(response)
        self.assertEqual(response.json()["errors"][0]["message"], "Object matching query does not exist.")
