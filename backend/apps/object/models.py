from django.db import models


class Object(models.Model):
    taken_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.id}"
