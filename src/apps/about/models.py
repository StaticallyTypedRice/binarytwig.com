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
        