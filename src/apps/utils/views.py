from django.shortcuts import render
from htmlmin.decorators import not_minified_response
from apps.utils.functions import parse_formatting

# Create your views here.

from .models import PrivacyPolicy, RobotsTxtModifications

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

@not_minified_response
def robots_txt(request):
    '''robots.txt page'''

    try:
        modifications = RobotsTxtModifications.objects.get()

        # If the modifications are not implemented, return None
        if not modifications.implemented:
            modifications = None
    except RobotsTxtModifications.DoesNotExist:
        modifications = None

    context = {
        'modifications': modifications,
    }

    return render(request, 'robots.txt', context, content_type='text/plain')
