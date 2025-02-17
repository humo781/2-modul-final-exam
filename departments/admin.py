from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_department', 'contact_email', 'contact_phone')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('created_at',)
    exclude = ('slug',)
