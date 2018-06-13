from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import About
from .forms import AboutForm

class AboutResource(resources.ModelResource):
    '''The model resource for the About model.'''

    class Meta:
        model = About

class AboutAdmin(admin.ModelAdmin):
    '''The admin page for the About model.'''

    resource_class = AboutResource

    list_display = [
        'time_edited',
    ]

    form = AboutForm

    def has_add_permission(self, request):
        '''Allow only one About page entry at a time.'''

        return not About.objects.exists()

admin.site.register(About, AboutAdmin)
