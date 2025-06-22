from django import forms
from .models import Event

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = [
            'slogan',
            'location',
            'start_time',
            'available_tickets',
            'key_features',
            'banner_url'
        ]

        widgets = {
            'slogan': forms.TextInput(attrs={
                'placeholder': 'Provide an appealing text...',
                'id': 'id_slogan',
                'maxlength': '120',
                'required': True,
            }),

            'location': forms.TextInput(attrs={
                'placeholder': '',
                'id': 'id_location',
                'maxlength': '120',
                'required': True,
            }),

            'start_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'id': 'id_start_time',
                'required': True,
            }),

            'available_tickets': forms.NumberInput(attrs={
                'placeholder': '',
                'id': 'id_available_tickets',
                'required': True,
                'min': 0
            }),

            'key_features': forms.Textarea(attrs={
                'placeholder': 'Provide important event details...',
                'id': 'id_key_features',
            }),

            'banner_url': forms.URLInput(attrs={
                'placeholder': 'An optional banner image URL...',
                'id': 'id_banner_url',
            }),
        }
