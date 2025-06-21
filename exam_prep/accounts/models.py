from django.core.validators import MinLengthValidator
from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
import re

def letters_only_validator(value):
    if not re.match(r'^[A-Za-z]+$', value):
        raise ValidationError("Your name must contain letters only!")

def passcode_validator(value):
    if not re.match(r'^\d{6}$', value):
        raise ValidationError("Your passcode must be exactly 6 digits!")

class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),  # No custom error message, uses Django default
            letters_only_validator,
        ]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            letters_only_validator,
        ]
    )

    passcode = models.CharField(
        max_length=6,
        validators=[
            passcode_validator,
        ],
        help_text="Your passcode must be a combination of 6 digits"
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank=True,
        null=True
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"