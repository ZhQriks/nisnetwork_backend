from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from app.api.classrooms.serializers import ClassroomSerializer
from app.api.classrooms.models import Classroom
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated

class ClassroomViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(detail=False, methods=["post"])
    def create_class(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            classRoom = serializer.save()
            if classRoom:
                return Response({'message': 'Classroom schedule created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def get_classes(self, request):
        group_number = request.query_params.get('group_number')
        week_day = request.query_params.get('week_day')
        classes = ClassroomSchedule.objects.all()

        if group_number is not None:
            classes = classes.filter(group_number=group_number)
        if week_day is not None:
            classes = classes.filter(week_day=week_day)

        class_serializer = ClassroomScheduleSerializer(classes, many=True)
        return Response(class_serializer.data)

    @action(detail=True, methods=["get"])
    def get_class(self, request, pk=None):
        try:
            classRoom = ClassroomSchedule.objects.get(pk=pk)
        except ClassroomSchedule.DoesNotExist:
            return Response({'message': 'Classroom schedule not found'}, status=status.HTTP_404_NOT_FOUND)
        class_serializer = ClassroomScheduleSerializer(classRoom)
        return Response(class_serializer.data)
