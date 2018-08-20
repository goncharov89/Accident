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
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accident_list, name='accident_list'),
    path('accident_detail/<int:pk>', views.accident_detail, name='accident_detail'),
    path('accident/new/', views.accident_new, name='accident_new'),
    path('event/new/<int:pk>', views.event_new, name='event_new'),
    path('event/link/<int:pk>', views.link_new, name='link_new'),
    path('accident/edit/<int:pk>', views.accident_edit, name='edit'),
    path('accident/pdf/<int:pk>', views.HelloPDFView.as_view(), name='pdf'),
    path('accident/nopdf/<int:pk>', views.nopdf, name='nopdf'),
]
