from django.shortcuts import render
from apps.utils.functions import parse_formatting

# Create your views here.

from apps.blog.models import Article

from .models import About

def home(request):
    '''Homepage'''

    # Get the first five articles that are visible and have thumbnails
    articles = Article.objects.filter(visible=True).order_by('-time_created')[:5]

    context = {
        'articles': articles,
        'navbar': {
            'selected': 'home',
        },
    }
    return render(request, 'home.html', context)

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
