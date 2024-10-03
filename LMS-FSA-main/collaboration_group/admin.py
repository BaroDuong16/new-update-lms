from django.contrib import admin

# Register your models here.
from .models import CollaborationGroup
class CollaborationGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'created_by', 'subject', 'created_at')