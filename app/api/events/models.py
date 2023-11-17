from django.db import models
from app.utils.base_model import BaseModel


class EventCalendar(BaseModel):
    color = models.CharField(max_length=7)
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=255)
    allday = models.BooleanField(default=False)
    description = models.TextField()


    def __str__(self):
            return self.title

    def create_event(self, validated_data):
        blog = self.model(**validated_data)
        blog.save()

        return blog
