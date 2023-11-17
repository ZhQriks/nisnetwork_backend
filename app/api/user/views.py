from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.http import Http404

from app.api.user.serializers import UserSerializer
from app.api.user.models import User
from app.utils.snippets import ModelViewSet


class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    @action(detail=False, methods=["post"])
    def create_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response({'message': 'Created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def current_user(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user_serializer = UserSerializer(user, many=False)
            data = user_serializer.data

            return Response(data)
        else:
            raise Http404("User not found")
