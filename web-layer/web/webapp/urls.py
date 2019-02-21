from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.conf.urls import url
import re

urlpatterns = [
 	path('admin/', admin.site.urls),
 	path('', views.displayStocks, name='index')
]