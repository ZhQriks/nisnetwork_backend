from django.contrib import admin
from app.api.classrooms.models import Classroom

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('subject', 'classroom', 'group_number', 'teacher_name', 'class_order', 'week_day', 'grade', 'grade_letter')  # Fields to display in the admin list
    list_filter = ('grade', 'subject', 'grade_letter')  # Filters on the right sidebar
    search_fields = ['subject', 'classroom', 'grade']  # Fields to search in the admin

admin.site.register(Classroom, ClassroomAdmin)
