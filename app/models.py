from django.db import models
from utils.models import TimestampedModel


class Room(TimestampedModel):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return self.name


class Meeting(TimestampedModel):
    title = models.CharField(max_length=255)
    duration = models.IntegerField(default=1)
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='meetings')

    def __str__(self):
        return self.title
