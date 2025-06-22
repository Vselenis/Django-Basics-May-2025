from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from organizers.models import Organizer



def validate_slogan_length(value):
    if not (2 <= len(value) <= 120):
        raise ValidationError(
            f"Ensure this value has between 2 and 120 characters (it has {len(value)})."
        )



def validate_location_length(value):
    if not (2 <= len(value) <= 120):
        raise ValidationError(
            f"Ensure this value has between 2 and 120 characters (it has {len(value)})."
        )



def validate_available_tickets(value):
    if value < 0:
        raise ValidationError("Ensure this value is greater than or equal to 0.")


class Event(models.Model):
    slogan = models.CharField(
        max_length=120,
        validators=[
            validate_slogan_length
        ],
    )

    location = models.CharField(
        max_length=120,
        validators=[
            validate_location_length
        ]
    )

    start_time = models.DateTimeField(
        default=timezone.now,
    )

    available_tickets = models.IntegerField(
        validators=[
            validate_available_tickets
        ],

    )
    key_features = models.TextField(
        blank=True,
        null=True
    )

    banner_url = models.URLField(
        blank=True,
        null=True
    )

    organizer = models.ForeignKey(
        Organizer,
        on_delete=models.CASCADE,
        editable=False
    )
