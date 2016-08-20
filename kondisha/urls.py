"""kondisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from rollyourown.seo.admin import register_seo_admin
from main.seopy import MyMetadata
from main import views

register_seo_admin(admin.site, MyMetadata)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^main/', include("main.urls")),
	url(r'^$', views.index, name="name"),
	url(r'^blog', include("pinax.blog.urls", namespace="pinax_blog")),
	#url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


urlpatterns += staticfiles_urlpatterns()
#urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
