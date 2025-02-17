from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'credit_hours')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('created_at',)
    exclude = ('slug',)
