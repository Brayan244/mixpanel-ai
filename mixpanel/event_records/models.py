from django.db import models
from pgvector.django import VectorField

class EventRecord(models.Model):
    """A record of an event that has occurred."""
    # The name of the event.
    name = models.CharField(max_length=255)
    # The description of the event.
    description = models.TextField()
    embedding = VectorField(dimensions=1536)