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
    path('add/', views.addStock, name='add'),
    path('search/', views.searchStock, name='search'),
    path('logout/', views.logout, name='logout'),
    re_path(r'^user/(?P<uniqueID>[0-9]+)$',
            views.userDetail, name='user_detail'),
    re_path(r'^stock/(?P<uniqueID>[0-9]+)$',
            views.stockDetail, name='stock_detail')
]
