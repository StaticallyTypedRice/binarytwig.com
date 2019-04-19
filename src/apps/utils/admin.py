from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import PrivacyPolicy, HtmlModifications, RobotsTxtModifications
from .forms import PrivacyPolicyForm, HtmlModificationsForm, RobotsTxtModificationsForm

class PrivacyPolicyResource(resources.ModelResource):
    '''The model resource for the PrivacyPolicy model.'''

    class Meta:
        model = PrivacyPolicy

class HtmlModificationsResource(resources.ModelResource):
    '''The model resource for the HtmlModifications model.'''

    class Meta:
        model = HtmlModifications

class RobotsTxtModificationsResource(resources.ModelResource):
    '''The model resource for the RobotsTxtModifications model.'''

    class Meta:
        model = RobotsTxtModifications

class PrivacyPolicyAdmin(admin.ModelAdmin):
    '''The admin page for the PrivacyPolicy model.'''

    resource_class = PrivacyPolicyResource

    list_display = [
        'time_edited',
        'current',
    ]

    form = PrivacyPolicyForm

class HtmlModificationsAdmin(admin.ModelAdmin):
    '''The admin page for the HtmlModifications model.'''

    resource_class = HtmlModificationsResource

    list_display = [
        'time_edited',
        'implemented',
    ]

    form = HtmlModificationsForm

    def has_add_permission(self, request):
        '''Allow only one HTML modifications entry at a time.'''

        return not self.model.objects.exists()

class RobotsTxtModificationsAdmin(admin.ModelAdmin):
    '''The admin page for the RobotsTxtModifications model.'''

    resource_class = RobotsTxtModificationsResource

    list_display = [
        'time_edited',
        'implemented',
    ]

    form = RobotsTxtModificationsForm

    def has_add_permission(self, request):
        '''Allow only one robots.txt modifications entry at a time.'''

        return not self.model.objects.exists()

admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
admin.site.register(HtmlModifications, HtmlModificationsAdmin)
admin.site.register(RobotsTxtModifications, RobotsTxtModificationsAdmin)
