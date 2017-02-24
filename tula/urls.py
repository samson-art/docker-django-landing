"""tula URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

import tula.views as myviews
from tula import settings
from filebrowser.sites import site

# site.storage.location = 'assets/'

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', myviews.landing_page, name='landing_page'),
    url(r'^portfolio/weddings', myviews.weddings, name='weddings'),
    url(r'^portfolio/graduation', myviews.graduation, name='graduation'),
    url(r'^portfolio/bdays', myviews.bdays, name='bdays'),
    url(r'^portfolio/kids', myviews.kids, name='kids'),
    url(r'^about/', myviews.about, name='about'),
    url(r'^price/', myviews.price, name='price')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
