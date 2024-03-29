"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve
from django.conf.urls import url

admin.site.site_header="Filox Admin"
admin.site.site_title="Filox Admin Panel"
admin.site.index_title="Welcome to Filox Admin Panel"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('healthblog.urls')),
    path('doctor/', include('doctor.urls')),
    path('',views.home,name='projecthome'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

