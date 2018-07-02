from django.conf import settings

def website_mode(request):
    '''Obtains the mode of the website from the site settings.

    Creates a context variable called 'website_mode'.
    '''

    return {'website_mode': settings.MODE}

def google_web_utils(request):
    '''Obtains Google webmaster tools configuration from settings.

    Creates a variables called 'google_site_verification'..
    '''
    
    try:
        google_site_verification = settings.GOOGLE_SITE_VERIFICATION
    except:
        google_site_verification = ''

    return {
        'google_site_verification': google_site_verification,
    }
