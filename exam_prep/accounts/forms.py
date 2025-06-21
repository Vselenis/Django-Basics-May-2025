from django import forms
from .models import Author

class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number', 'info', 'image_url']
        widgets = {
            'passcode': forms.PasswordInput(attrs={
                'placeholder': 'Enter 6 digits...',
                'aria-describedby': 'id_passcode_helptext'
            }),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
            'info': forms.Textarea(attrs={'placeholder': 'Some funny info of me and all my pets', 'rows': 3}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://your-photo-link.com'}),
        }
        help_texts = {
            'passcode': 'Your passcode must be a combination of 6 digits'
        }