import uuid
from django.db import models


# Create your models here.
class Game(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    steamapp_id = models.IntegerField()
    name = models.TextField()
    thumbnail = models.TextField()
    cheapest_deal_id = models.TextField(blank=True, default="")
    cheapest_deal_price = models.FloatField(null=True)

    def __str__(self) -> str:
        return f"Game title: {self.name}; steamapp ID: {self.steamapp_id}"
