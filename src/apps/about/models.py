from django.db import models

# Create your models here.

class About(models.Model):
    '''The model for the About page content.'''

    content = models.CharField(max_length=500000, blank=False, null=False,
                               help_text='The page content.')

    markdown = models.BooleanField(null=False, default=True,
                                   help_text='If True, Markdown formatting will be enabled.')
    html = models.BooleanField(null=False, default=True, help_text='If True, HTML will be enabled.')

    visible = models.BooleanField(null=False, default=False,
                                  help_text='If False, this page will not be publically visible.')

    time_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'About page content'
        verbose_name_plural = 'About page content'

    def __str__(self):
        return self.content
        