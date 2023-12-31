from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export.admin import ImportExportModelAdmin
from app.api.user.models import User
from app.api.classroom.models import Classroom
from app.api.events.models import EventCalendar
from django.utils.translation import gettext as _


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'first_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    pass

@admin.register(EventCalendar)
