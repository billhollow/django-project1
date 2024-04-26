from django.contrib import admin

from simple_cruds.student.admin import StudentAdmin
from simple_cruds.student.models import Student

# Register your models here.

admin.site.register(Student, StudentAdmin)
