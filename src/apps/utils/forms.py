from django import forms

from .models import PrivacyPolicy

class PrivacyPolicyForm(forms.ModelForm):
    '''The form for the PrivacyPolicy model.'''

    class Meta:
        model = PrivacyPolicy
        fields = [
            'content',
            'current',
        ]
        widgets = {
            'content': forms.Textarea(attrs={
                'cols': 125,
                'rows': 40,
            }),
        }
