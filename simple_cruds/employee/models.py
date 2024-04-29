from django.db import models
from django.db.models.functions import Lower

from simple_cruds.employee.choices import GenderChoices


class Employee(models.Model):
    firstName = models.CharField(max_length=255, blank=False)
    lastName = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    dob = models.DateField(max_length=254, blank=False)
    gender = models.CharField(max_length=255, choices=GenderChoices)
    educationLevel = models.CharField(max_length=255, blank=False)
    workExperience = models.PositiveIntegerField()
    salary = models.PositiveIntegerField()

    class Meta:
        db_table = "simp_crud_empl"

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
