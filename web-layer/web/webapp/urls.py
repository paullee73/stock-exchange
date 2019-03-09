from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.conf.urls import url
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.displayHome, name='index'),
    path('login/', views.displayLogIn, name='login'),
    path('signup/', views.displaySignUp, name='signup'),
    path('stocks/', views.displayStocks, name='stocks'),
    re_path(r'^user/(?P<uniqueID>[0-9]+)$',
            views.userDetail, name='user_detail')
]
