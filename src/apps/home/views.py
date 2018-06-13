from django.shortcuts import render

# Create your views here.

from apps.blog.models import Article

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
