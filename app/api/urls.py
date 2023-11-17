from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from app.api.user import views as user_views
from app.api.blog.views import BlogViewSet
from app.api.events.views import EventViewSet

from app.api.classrooms.views import ClassroomViewSet
urlpatterns = [
    path('blog/create', BlogViewSet.as_view({'post': 'create_blog'}), name='create_blog'),
    path('blog/', BlogViewSet.as_view({'get': 'get_blogs'}), name='get_blogs'),
    path('blog/<int:pk>/', BlogViewSet.as_view({'get': 'get_blog'}), name='get_blog'),

    path('events/create', EventViewSet.as_view({'post': 'create_event'}), name='create_event'),
    path('events/', EventViewSet.as_view({'get': 'get_events'}), name='get_events'),
    path('events/<int:pk>/', EventViewSet.as_view({'get': 'get_event'}), name='get_event'),

    path('classrooms/create', ClassroomViewSet.as_view({'post': 'create_class'}), name='create_classroom'),
    path('classrooms/', ClassroomViewSet.as_view({'get': 'get_classes'}), name='get_classrooms'),
    path('classrooms/<int:pk>/', ClassroomViewSet.as_view({'get': 'get_class'}), name='get_classroom'),
]
