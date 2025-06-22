from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

import re


def validate_company_name(value):
    if not re.fullmatch(r'[A-Za-z0-9\- ]+', value):
        raise ValidationError("The company name is invalid!")


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError("Phone number must contain digits only.")
    if len(value) > 15:
        raise ValidationError("Enter a valid phone number (up to 15 digits).")

def validate_secret_key(value):
    if len(value) != 4 or not value.isdigit() or len(set(value)) != 4:
        raise ValidationError("Your secret key must have 4 unique digits!")



class Organizer(models.Model):
    company_name = models.CharField(
        max_length=110,
        unique=True,
        validators=[
            MinLengthValidator(2),
            validate_company_name,
        ],
        help_text="*Allowed names contain letters, digits, spaces, and hyphens."
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            validate_phone_number,
        ]
    )

    secret_key = models.CharField(
        max_length=4,
        validators=[
            validate_secret_key,
        ],
        help_text="*Pick a combination of 4 unique digits.",
    )

    website = models.URLField(
        blank=True,
        null=True
    )


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['phone_number'],
                name='unique_phone_number',
                violation_error_message="That phone number is already in use!"
            )
        ]

