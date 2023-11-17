from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from app.api.events.serializers import EventSerializer
from app.api.events.models import EventCalendar
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated


class EventViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(detail=False, methods=["post"])
    def create_event(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            if event:
                return Response({'message': 'Event created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def get_events(self, request):
        events = EventCalendar.objects.all()
        event_serializer = EventSerializer(events, many=True)
        return Response(event_serializer.data)

    @action(detail=False, methods=["get"])
    def get_event(self, request, pk=None):
        try:
            event = EventCalendar.objects.get(pk=pk)
        except EventCalendar.DoesNotExist:
            return Response({'message': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        event_serializer = EventSerializer(event)
        return Response(event_serializer.data)
