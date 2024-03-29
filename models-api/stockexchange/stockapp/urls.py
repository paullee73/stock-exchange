"""techrent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from stockapp import views
from django.conf.urls import url
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    re_path(r'^user/create', views.CreateUser),
    re_path(r'^user/(?P<uniqueID>[0-9]+)$', views.ViewOrUpdateUser),
    re_path(r'^user/(?P<uniqueID>[0-9]+)/delete$', views.DeleteUser),

    re_path(r'^stock/item_detail$', views.SelectAllStock),
    re_path(r'^stock/create$', views.CreateStock),
    re_path(r'^stock/(?P<uniqueID>[0-9]+)$', views.ViewOrUpdateStock),
    re_path(r'^stock/(?P<uniqueID>[0-9]+)/delete$', views.DeleteStock),

    re_path(r'^create/authentication', views.CreateAuthentication),
    re_path(
        r'^search/authentication/(?P<hashed>[a-z0-9]+)$', views.SearchAuthentication),
    re_path(r'^logout', views.Logout),
]
