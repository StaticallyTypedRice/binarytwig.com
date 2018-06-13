from django import forms

from .models import ExternalSite

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
