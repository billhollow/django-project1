from django.contrib import admin

from simple_cruds.student.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'email', 'phone']
    ordering = ['id']
    search_fields = ['id', 'name', 'course', 'email', 'phone']
    