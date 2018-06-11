from django import forms

from .models import About, ExternalSite

class AboutForm(forms.ModelForm):
    '''The form for the About model.'''

    class Meta:
        model = About
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.Textarea(attrs={
                'cols': 125,
                'rows': 40,
            }),
        }

class ExternalSiteForm(forms.ModelForm):
    '''The form for the ExternalSite model.'''

    class Meta:
        model = ExternalSite
        fields = [
            'name',
            'icon',
            'url',
            'new_tab',
            'visible',
        ]
