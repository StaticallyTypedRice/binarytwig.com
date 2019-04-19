from django.db import models

# Create your models here.

class PrivacyPolicy(models.Model):
    '''The model for the Privacy policy pages.'''

    content = models.TextField(max_length=500000, blank=False, null=False)

    current = models.BooleanField(null=False, default=True,
                                  help_text='Is this the current privacy policy?')

    time_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Privacy policy'
        verbose_name_plural = 'Privacy policy'

    def __str__(self):
        return str(self.time_edited)

class HtmlModifications(models.Model):
    '''The model for modifications to the HTML page.'''

    head = models.CharField(max_length=500000, blank=False, null=False,
                            help_text='These modifications will be placed in the head tag.')
    misc = models.CharField(max_length=500000, blank=False, null=False,
                            help_text='These modifications will be placed at the end of the body tag.')

    implemented = models.BooleanField(null=False, default=False,
                                      help_text='If False, these modifications will not be implemented.')

    time_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'HTML Modification'
        verbose_name_plural = 'HTML Modifications' 

class RobotsTxtModifications(models.Model):
    '''The model for modifications to the robots.txt page.'''

    modifications = models.CharField(max_length=500000, blank=False, null=False,
                                     help_text='These modifications will be placed at the end of the robots.txt file.')

    implemented = models.BooleanField(null=False, default=False,
                                      help_text='If False, these modifications will not be implemented.')

    time_edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'robots.txt Modification'
        verbose_name_plural = 'robots.txt Modifications' 
