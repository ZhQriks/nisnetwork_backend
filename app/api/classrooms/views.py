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
        grade = request.query_params.get('grade')
        grade_letter = request.query_params.get('grade_letter')
        classes = Classroom.objects.all()

        if group_number:
            if group_number == '1':
                classes = classes.exclude(group_number='2')
            elif group_number == '2':
                classes = classes.exclude(group_number='1')
            else:
                classes = classes.filter(group_number=group_number)
        if week_day is not None:
            classes = classes.filter(week_day=week_day)
        if grade is not None:
            classes = classes.filter(grade=grade)
        if grade_letter is not None:
            classes = classes.filter(grade_letter=grade_letter)

        class_serializer = ClassroomSerializer(classes, many=True)
        return Response(class_serializer.data)

    @action(detail=True, methods=["get"])
    def get_class(self, request, pk=None):
        try:
            classRoom = Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return Response({'message': 'Classroom schedule not found'}, status=status.HTTP_404_NOT_FOUND)
        class_serializer = ClassroomSerializer(classRoom)
        return Response(class_serializer.data)
