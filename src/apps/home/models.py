from django.db import models

# Create your models here.

class About(models.Model):
    '''The model for the About page content.'''

    content = models.CharField(max_length=500000, blank=False, null=False)

    time_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'About page content'
        verbose_name_plural = 'About page content'

    def __str__(self):
        return self.content

class ExternalSite(models.Model):
    '''The model for links to external websites, such as social media.'''

    name = models.CharField(max_length=50, blank=False, null=False,
                            help_text="The name that the link will appear as.")
    icon = models.CharField(max_length=200, blank=True, null=False,
                            help_text="The icon for the link (as an HTML snippet).")
    url = models.URLField(max_length=200, blank=False, null=False,
                          help_text="The URL of the external site.")

    new_tab = models.BooleanField(null=False, default=True,
                                  help_text="If True, the link will be opened in a new tab.")
    visible = models.BooleanField(null=False, default=True,
                                  help_text='If False, the link will not be publically visible.')

    time_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_edited = models.DateTimeField(auto_now_add=False, auto_now=True)
    