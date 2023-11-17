from django.db import models
from app.utils.base_model import BaseModel


class BlogPost(BaseModel):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image_url = models.CharField(max_length=300)
    content = models.TextField()

    def __str__(self):
        return self.title

    def create_blog(self, validated_data):
        blog = self.model(**validated_data)
        blog.save()

        return blog
