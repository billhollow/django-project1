from django.db import models
from django.db.models.functions import Lower


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255, blank=False)
    course = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "simp_crud_stud"
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='name'
            ),
        ]
