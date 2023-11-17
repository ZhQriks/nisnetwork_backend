from app.api.blog.models import BlogPost
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'author',
            'image_url',
            'content',
        ]

    def create_blog(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return BlogPost.objects.create_blog(**validated_data)
