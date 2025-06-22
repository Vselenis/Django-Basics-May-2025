from django import forms
from .models import Organizer

class OrganizerCreateForm(forms.ModelForm):
    class Meta:
        model = Organizer

        fields = [
            'company_name',
            'phone_number',
            'secret_key'
        ]

        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Enter a company name...',
                'maxlength': '110',
                'required': True,
                'aria-describedby': 'id_company_name_helptext',
                'id': 'id_company_name'
            }),

            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter a valid phone number (digits only)...',
                'maxlength': '15',
                'required': True,
                'id': 'id_phone_number'
            }),

            'secret_key': forms.PasswordInput(attrs={
                'placeholder': 'Enter a secret key like <1234>...',
                'maxlength': '4',
                'required': True,
                'aria-describedby': 'id_secret_key_helptext',
                'id': 'id_secret_key'
            }),

        }

class OrganizerEditForm(forms.ModelForm):
    class Meta:
        model = Organizer

        fields = [
            'company_name',
            'phone_number',
            'website'
        ]

        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': ''
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': ''
            }),
            'website': forms.URLInput(attrs={
                'placeholder': ''
            }),
        }

        help_texts = {
            'company_name': '*Allowed names contain letters, digits, spaces, and hyphens.',
        }