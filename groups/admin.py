from django.contrib import admin
from .models import Group, Schedule

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_year', 'max_students', 'grade_level')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('created_at',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
