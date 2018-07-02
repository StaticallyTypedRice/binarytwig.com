from django.conf import settings

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
    except NameError:
        google_site_verification = ''

    return {
        'google_site_verification': google_site_verification,
    }
