from django import forms

from .models import PrivacyPolicy, HtmlModifications

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

class HtmlModificationsForm(forms.ModelForm):
    '''The form for the HtmlModifications model.'''

    class Meta:
        model = HtmlModifications
        fields = [
            'head',
            'misc',
            'implemented',
        ]
        widgets = {
            'head': forms.Textarea(attrs={
                'cols': 125,
                'rows': 40,
            }),
            'misc': forms.Textarea(attrs={
                'cols': 125,
                'rows': 40,
            }),
        }
