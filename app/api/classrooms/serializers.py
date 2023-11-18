from app.api.classrooms.models import Classroom
from rest_framework import serializers

class ClassroomSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = Classroom
        fields = [
            'id',
            'subject',
            'classroom',
            'group_number',
            'teacher_name',
            'class_order',
            'week_day',
            'grade_letter',
            'grade',
        ]

    def create_classroom(self, validated_data):
        return Classroom.objects.create_classroom(**validated_data)
