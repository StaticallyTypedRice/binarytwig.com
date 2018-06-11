from django.conf import settings

def website_mode(request):
    '''Obtains the mode of the website from the site settings.

    Creates a context variable called 'website_mode'.
    '''

    return {'website_mode': settings.MODE}

def google_web_utils(request):
    '''Obtains Google webmaster tools and analytics configurations 
    from settings.

    Creates two context variables: 'google_site_verification'
    and 'google_analytics_id'.
    '''

    return {
        'google_site_verification': settings.GOOGLE_SITE_VERIFICATION,
        'google_analytics_id': settings.GOOGLE_ANALYTICS_ID,
    }
