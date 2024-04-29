from django.contrib import admin


class EmployeeAdmin(admin.ModelAdmin):
    ordering = ['id']
