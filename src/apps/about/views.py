from django.shortcuts import render
from apps.utils.functions import parse_formatting

# Create your views here.

from .models import About, ThirdPartyLicenses

def about_abstract(request, model, template, navbar_selected=False):
    '''Abstract function for the pages'''

    try:
        query = model.objects.all()

        content = None
        for c in query:
            content = c

        print(type(content))
        
        content.content = parse_formatting(content.content,
                                           html=content.html,
                                           markdown=content.markdown)

        # Only display the page if it has been set to 'visible'.
        if not content.visible:
            content = None
            
    except model.DoesNotExist:
        content = None

    context = {
        'content': content,
        'navbar': {
            'selected': "about" if navbar_selected else None,
        },
    }
    return render(request, template, context)

def about(request):
    '''About page'''

    return about_abstract(request, About, 'about.html', True)

def third_party_licenses(request):
    '''Third party licenses page'''

    return about_abstract(request, ThirdPartyLicenses, 
                          'third_party_licenses.html', False)
