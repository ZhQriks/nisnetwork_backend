from app.api.events.models import EventCalendar
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = EventCalendar
        fields = [
            'id',
            'color',
            'start',
            'end',
            'title',
            'allday',
            'description',
        ]

    def create_event(self, validated_data):
        return EventCalendar.objects.create_event(**validated_data)
