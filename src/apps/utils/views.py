from django.shortcuts import render
from apps.utils.functions import parse_formatting

# Create your views here.

from .models import PrivacyPolicy

def privacy_policy(request):
    '''Privacy policy page'''

    try:
        content = PrivacyPolicy.objects.filter(current=True
                                              ).order_by("-time_edited")[0]

        content.content = parse_formatting(content.content,
                                           html=True, markdown=True)
    except IndexError:
        content = None

    context = {
        'content': content,
        'navbar': {
            'selected': 'about',
        },
    }
    return render(request, 'privacy-policy.html', context)
