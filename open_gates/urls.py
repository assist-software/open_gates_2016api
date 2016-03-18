"""open_gates URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfileView
from files.views import AppFileView, AppFileViewSet, AppFileList

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/files/$', AppFileViewSet.as_view({'get': 'list'})),
    url(r'^api/files/user/(?P<pk>\d+)/$', AppFileList.as_view()),
    url(r'^api/files/upload/$', AppFileView.as_view()),
    url(r'^api/user/(?P<pk>\d+)/$', ProfileView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

