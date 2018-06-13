'''twigfusion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
'''
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Imports from views
from apps.home import views as home
from apps.about import views as about
from apps.utils import views as utils

# Regular webpages
pages = [

    # Homepage
    url(r'^$', home.home, name='home'),

    # About page
    url(r'^about/$', about.about, name='about'),
    url(r'^about/third-party-licenses/$', about.third_party_licenses,
        name='third_party_licenses'),

    # Blog
    url(r'^', include('apps.blog.urls')),

    # Admin pages
    url(r'^admin/', admin.site.urls),

    # Misc
    url(r'^about/privacy/$', utils.privacy_policy, name='privacy_policy'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='misc/robots.txt',
                                               content_type='text/plain')),

]

# API pages
apis = []

# Create the 'urlpatterns' list from 'pages' and 'apis'.
urlpatterns = pages + apis

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
