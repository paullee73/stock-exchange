from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
import urllib.request
import urllib.parse
import urllib.error
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return HttpResponse("Test")


def StockAll(request):
    if (request.method == 'GET'):
        req = urllib.request.Request(
            "http://models-api:8000/stockapp/stock/item_detail")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    return JsonResponse(resp)


def UserInf(request, uniqueID):
    if (request.method == 'GET'):
        req = urllib.request.Request(
            "http://models-api:8000/stockapp/user/" + uniqueID + "")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    return JsonResponse(resp)


@csrf_exempt
def CreateUser(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        balance = request.POST['balance']
        post_data = {'username': username,
                     'password': password, 'balance': balance}
        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request(
            "http://models-api:8000/stockapp/user/create", data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        return JsonResponse(resp)


@csrf_exempt
def LogIn(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        post_data = {'username': username,
                     'password': password}
        post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request(
            "http://models-api:8000/stockapp/create/authentication", data=post_encoded, method='POST')
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
        return JsonResponse(resp)
