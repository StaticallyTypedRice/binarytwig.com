from django.shortcuts import render
from apps.utils.functions import parse_formatting

# Create your views here.

from .models import About

def about(request):
    '''About page'''

    try:
        content = About.objects.get()
        content.content = parse_formatting(content.content,
                                           html=True, markdown=True)
    except About.DoesNotExist:
        content = None

    context = {
        'content': content,
        'navbar': {
            'selected': 'about',
        },
    }
    return render(request, 'about.html', context)
