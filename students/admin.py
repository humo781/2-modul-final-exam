from django.contrib import admin
from .models import Student, Grade, Gender, ParentGuardian

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'enrollment_date', 'group', 'department')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
    ordering = ('created_at',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ParentGuardian)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'relationship', 'student')
