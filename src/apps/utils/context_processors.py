from django.conf import settings

from .models import HtmlModifications

def website_name(request):
    '''Obtains the website name information from the site settings.

    Creates the context variables 'website_name', 'website_name_stylized' and 'website_name_slug'
    '''

    try:
        website_name = settings.WEBSITE_NAME
    except NameError:
        website_name = ''

    try:
        website_name_stylized = settings.WEBSITE_NAME_STYLIZED
    except NameError:
        # If the stylized website name is not set, fall back to the unstylized name.
        website_name_stylized = website_name

    return {
        'website_name': website_name,
        'website_name_stylized': website_name_stylized,
        'wesbite_name_slug': settings.WEBSITE_NAME_SLUG,
    }
def website_mode(request):
    '''Obtains the mode and configuration message of the website from the site settings.

    Creates the context variables 'website_mode' and 'website_config_message'.
    '''

    try:
        website_config_message = settings.CONFIGURATION_FILE_MESSAGE
    except NameError:
        website_config_message = ''

    return {
        'website_mode': settings.MODE,
        'website_config_message': website_config_message,
    }

def google_web_utils(request):
    '''Obtains Google webmaster tools configuration from settings.

    Creates a context variable called 'google_site_verification'.
    '''

    try:
        google_site_verification = settings.GOOGLE_SITE_VERIFICATION
    except AttributeError:
        google_site_verification = ''

    return {
        'google_site_verification': google_site_verification,
    }

def html_modifications(request):
    '''Gets the HTML modifications from the database.

    Creates a context variable called 'html_modifications'.
    '''

    # Return empty strings if no modifications are present
    no_modifications = {
        'head': '',
        'tail': '',
    }
    
    try:
        html_modifications = HtmlModifications.objects.get()

        # If the modifications are not implemented, return empty strings
        if not html_modifications.implemented:
            html_modifications = no_modifications

    except HtmlModifications.DoesNotExist:
        html_modifications = no_modifications

    return {'html_modifications': html_modifications}
