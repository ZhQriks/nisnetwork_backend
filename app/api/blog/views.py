from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from app.api.blog.serializers import BlogSerializer
from app.api.blog.models import BlogPost
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated


class BlogViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(detail=False, methods=["post"])
    def create_blog(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            blog = serializer.save()
            if blog:
                return Response({'message': 'Blog created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def get_blogs(self, request):
        blogs = BlogPost.objects.all()
        blog_serializer = BlogSerializer(blogs, many=True)
        return Response(blog_serializer.data)

    @action(detail=False, methods=["get"])
    def get_blog(self, request, pk=None):
        try:
            blog = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        blog_serializer = BlogSerializer(blog)
        return Response(blog_serializer.data)
