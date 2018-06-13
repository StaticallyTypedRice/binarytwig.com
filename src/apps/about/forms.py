from django import forms

from .models import About

class AboutForm(forms.ModelForm):
    '''The form for the About model.'''

    class Meta:
        model = About
        fields = [
            'content',
            'markdown',
            'html',
            'visible',
        ]
        widgets = {
            'content': forms.Textarea(attrs={
                'cols': 125,
                'rows': 40,
            }),
        }

class ThirdPartyLicensesForm(AboutForm):
    '''The form for the ThirdPartyLicenses model.'''
