from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderChoices(models.TextChoices):
    MALE = "male", _("male")
    FEMALE = "female", _("female")
