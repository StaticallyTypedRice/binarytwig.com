from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import PrivacyPolicy
from .forms import PrivacyPolicyForm

class PrivacyPolicyResource(resources.ModelResource):
    '''The model resource for the PrivacyPolicy model.'''

    class Meta:
        model = PrivacyPolicy

class PrivacyPolicyAdmin(admin.ModelAdmin):
    '''The admin page for the PrivacyPolicy model.'''

    resource_class = PrivacyPolicyResource

    list_display = [
        'time_edited',
        'current',
    ]

    form = PrivacyPolicyForm

admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
