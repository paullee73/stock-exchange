from django.contrib import admin
from django.urls import path, re_path, include
from exp_api import views
from django.conf.urls import url
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^stock/item_detail$', views.StockAll),
    re_path(r'^user/(?P<uniqueID>[0-9]+)$', views.UserInf),
    re_path(r'^user/create', views.CreateUser),
    re_path(r'^user/login', views.LogIn),
]
