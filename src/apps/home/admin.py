from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import ExternalSite
from .forms import ExternalSiteForm

class ExternalSiteResource(resources.ModelResource):
    '''The model resource for the ExternalSite model.'''

    class Meta:
        model = ExternalSite

class ExternalSiteAdmin(admin.ModelAdmin):
    '''The admin page for the ExternalSite model.'''

    resource_class = ExternalSiteResource

    list_display = [
        'name',
        'url',
        'visible',
    ]

    form = ExternalSiteForm

admin.site.register(ExternalSite, ExternalSiteAdmin)
