"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.accident_list, name='accident_list'),
    url(r'^accident_detail/(?P<pk>\d+)/$', views.accident_detail, name='accident_detail'),
    url(r'^accident/new/$', views.accident_new, name='accident_new'),
    url(r'^event/new/(?P<pk>\d+)/$', views.event_new, name='event_new'),
    url(r'^event/link/(?P<pk>\d+)/$', views.link_new, name='link_new'),
    url(r'^accident/edit/(?P<pk>\d+)/$', views.accident_edit, name='edit'),
]
