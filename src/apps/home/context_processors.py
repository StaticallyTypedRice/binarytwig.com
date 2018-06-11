from .models import ExternalSite

def external_sites(request):
    '''Gets the list of extrenal site links.

    Creates a context variable called 'external_sites'.
    '''
    
    links = ExternalSite.objects.filter(visible=True)

    return {'external_sites': links}
