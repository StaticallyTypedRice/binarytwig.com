from django.conf import settings

from .models import HtmlModifications

def website_mode(request):
    '''Obtains the mode of the website from the site settings.

    Creates a context variable called 'website_mode'.
    '''

    return {'website_mode': settings.MODE}

def google_web_utils(request):
    '''Obtains Google webmaster tools configuration from settings.

    Creates a context variable called 'google_site_verification'..
    '''

    return {
        'google_site_verification': settings.GOOGLE_SITE_VERIFICATION,
    }

def html_modifications(request):
    '''Gets the HTML modifications from the database.

    Creates a context variable called 'html_modifications'.
    '''
    
    html_modifications = HtmlModifications.objects.get()

    # If the modifications are not implemented, return empty strings
    if not html_modifications.implemented:
        html_modifications = {
            'head': '',
            'tail': '',
        }

    return {'html_modifications': html_modifications}
