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
