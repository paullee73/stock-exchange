from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
import urllib.request
import urllib.parse
import urllib.error
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from webapp.forms import SignUpForm, StockForm

# Create your views here.


def addStock(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return render(request, 'login.html')
    if(request.method == 'POST'):
        form = StockForm(request.POST)
        if(form.is_valid()):
            ticker = form.cleaned_data.get('ticker')
            post_data = {}
            post_data['ticker'] = ticker
            post_data['auth'] = auth
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request(
                "http://exp-api:8000/exp/stock/create", data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            if 'ERROR' in resp:
                return render(request, 'error.html', {'error': 'Invalid authentication'})
            else:
                return render(request, 'item_detail.html')
    else:
        form = StockForm()
        return render(request, 'create_stock.html', {'form': form})


def displayHome(request):
    if(request.method == 'GET'):
        return render(request, 'index.html')


def displayLogIn(request):
    if(request.method == 'POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            post_data = {'username': username,
                         'password': password}
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request(
                "http://exp-api:8000/exp/user/login", data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            if 'GOOD' in resp:
                response = render(request, 'login.html', {'loggedIn': 'Welcome ' + username + '!'})
                response.set_cookie("auth", resp['auth'])
                return response
            else:
                return render(request, 'error.html', {'error': 'Incorrect credentials'})
    else:
        form = SignUpForm()
        return render(request, 'login.html', {'form': form})


def displaySignUp(request):
    if(request.method == 'POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            post_data = {'username': username,
                         'password': password, 'balance': 0}
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request(
                "http://exp-api:8000/exp/user/create", data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def displayStocks(request):
    if (request.method == 'GET'):
        req = urllib.request.Request(
            "http://exp-api:8000/exp/stock/item_detail")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        resplist = resp['data']
    return render(request, 'item_detail.html', {'resplist': resplist})


def logout(request):
    auth = request.COOKIES['auth']
    if not auth:
        return render(request, 'login.html')
    post_data = {'auth': auth}
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request(
        "http://exp-api:8000/exp/logout", data=post_encoded, method='POST')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    respauth = resp['auth']
    return HttpResponse(respauth)


def userDetail(request, uniqueID):
    if (request.method == 'GET'):
        req = urllib.request.Request(
            "http://exp-api:8000/exp/user/" + uniqueID + "")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    return render(request, 'user_detail.html', {'resp': resp})
