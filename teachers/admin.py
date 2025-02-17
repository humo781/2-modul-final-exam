from django.contrib import admin
from .models import Teacher, EmploymentType

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'qualification', 'phone_number', 'employment_type')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
    ordering = ('created_at',)
    # exclude = ('slug',)

@admin.register(EmploymentType)
class EmploymentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
