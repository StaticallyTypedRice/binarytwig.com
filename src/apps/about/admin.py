from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import About, ThirdPartyLicenses
from .forms import AboutForm, ThirdPartyLicensesForm

class AboutResource(resources.ModelResource):
    '''The model resource for the About model.'''

    class Meta:
        model = About

class ThirdPartyLicensesResource(AboutResource):
    '''The model resource for the ThirdPartyLicenses model.'''

    class Meta:
        model = ThirdPartyLicenses

class AboutAdmin(admin.ModelAdmin):
    '''The admin page for the About model.'''

    resource_class = AboutResource

    list_display = [
        'time_edited',
    ]

    form = AboutForm

    model = About

    def has_add_permission(self, request):
        '''Allow only one About page entry at a time.'''

        return not self.model.objects.exists()

class ThirdPartyLicensesAdmin(AboutAdmin):
    '''The admin page for the ThirdPartyLicenses model.'''

    resource_class = AboutResource

    form = AboutForm

    model = ThirdPartyLicenses

admin.site.register(About, AboutAdmin)
admin.site.register(ThirdPartyLicenses, ThirdPartyLicensesAdmin)
