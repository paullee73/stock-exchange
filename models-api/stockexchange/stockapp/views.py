from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from .models import User, Stock, Authenticator
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
import os
import hmac
from django.conf import settings
from django.contrib.auth.hashers import *
import datetime


def index(request):
    return HttpResponse("Test")


def CreateAuthentication(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            authenticator = hmac.new(
                key=settings.SECRET_KEY.encode('utf-8'),
                msg=os.urandom(32),
                digestmod='sha256',
            ).hexdigest()
            if check_password(password, user.password):
                new_auth = Authenticator(
                    user_id=user.id, authenticator=authenticator, date_created=datetime.date.today())
                new_auth.save()
                data = {}
                data['GOOD'] = 'Signed in'
                data['auth'] = authenticator
                return JsonResponse(data)
            else:
                return JsonResponse({'ERROR': 'Invalid input'})
        except ObjectDoesNotExist:
            return JsonResponse({'ERROR': 'No user'})


def CreateUser(request):
    if(request.method == "POST"):
        username = request.POST['username']
        unpassword = request.POST['password']
        password = make_password(unpassword)
        balance = request.POST['balance']
        if(len(username) == 0 or len(password) == 0 or not balance.isdigit()):
            return JsonResponse({'ERROR': 'Invalid input'})

        newUser = User(username=username, password=password,
                       balance=float(balance))
        newUser.save()

        return JsonResponse({'username': username, 'password': unpassword, 'balance': balance})


def ViewOrUpdateUser(request, uniqueID):
    if(request.method == "GET"):
        try:
            user = User.objects.get(pk=uniqueID)
        except ObjectDoesNotExist:
            return JsonResponse({'ERROR': 'Object with ID does not exist'})
        user = User.objects.get(pk=uniqueID)
        username = user.username
        password = user.password
        balance = user.balance
        return JsonResponse({'username': username, 'password': password, 'balance': balance})

    if(request.method == "POST"):
        userToUpdate = User.objects.get(pk=uniqueID)
        username = request.POST['username']
        password = request.POST['password']
        balance = request.POST['balance']

        if(len(username) != 0):
            userToUpdate.username = username
        if(len(password) != 0):
            userToUpdate.password = password
        if(len(balance) != 0):
            if(not balance.isdigit()):
                return JsonResponse({'ERROR': 'Invalid input'})
            userToUpdate.balance = balance

        userToUpdate.save()

        return JsonResponse({'username': username, 'password': password, 'balance': balance})


def DeleteUser(request, uniqueID):
    if(request.method == "POST"):
        try:
            user = User.objects.get(pk=uniqueID)
        except ObjectDoesNotExist:
            return JsonResponse({'ERROR': 'Object with ID does not exist'})
        userToDelete = User.objects.get(pk=uniqueID)
        username = userToDelete.username
        password = userToDelete.password
        balance = userToDelete.balance
        userToDelete.delete()
        return JsonResponse({'username': username, 'password': password, 'balance': balance})


def CreateStock(request):
    if(request.method == "POST"):
        auth = None
        ticker = request.POST['ticker']
        auth = request.POST['auth']
        if(len(ticker) == 0):
            return JsonResponse({'ERROR': 'Invalid input'})
        try:
            auth = Authenticator.objects.get(authenticator=auth)
        except ObjectDoesNotExist:
            return JsonResponse({'ERROR': 'Not authenticated'})
        newStock = Stock(ticker_sym=ticker, user_id=auth.user_id)
        newStock.save()
        return JsonResponse({'ticker symbol': ticker, 'owner': auth.user_id, 'id': newStock.id})


def ViewOrUpdateStock(request, uniqueID):
    if(request.method == "GET"):
        try:
            stock = Stock.objects.get(pk=uniqueID)
        except ObjectDoesNotExist:
            return JsonResponse({'ERROR': 'Object with ID does not exist'})
        ticker = stock.ticker_sym
        user = stock.user
        return JsonResponse({'ticker symbol': ticker, 'owner': user.id})

    if(request.method == "POST"):
        stockToUpdate = Stock.objects.get(pk=uniqueID)
        ticker = request.POST['ticker']
        user_id = request.POST['user_id']
        if(len(ticker) != 0):
            stockToUpdate.ticker_sym = ticker
        if(len(user_id) != 0):
            try:
                user = User.objects.get(pk=user_id)
            except ObjectDoesNotExist:
                return JsonResponse({'ERROR': 'User with that ID does not exist'})
            stockToUpdate.user = user
        stockToUpdate.save()
        return JsonResponse({'ticker': ticker, 'user': user_id})


def DeleteStock(request, uniqueID):
    if(request.method == "POST"):
        try:
            stock = Stock.objects.get(pk=uniqueID)
        except ObjectDoesNotExist:
            return JsonResponse({'ERROR': 'Object with ID does not exist'})
        stockToDelete = Stock.objects.get(pk=uniqueID)
        ticker = stockToDelete.ticker_sym
        owner = stockToDelete.user
        stockToDelete.delete()
        return JsonResponse({'ticker': ticker, 'user': owner.id})


def Logout(request):
    data = {}
    if(request.method == "POST"):
        auth = request.POST.get('auth')
        authDelete = Authenticator.objects.get(authenticator=auth)
        uid = authDelete.authenticator
        authDelete.delete()
        data['auth'] = uid
        return JsonResponse(data)


def SelectAllStock(request):
    if(request.method == "GET"):
        data = list(Stock.objects.all().values())
    return JsonResponse({'data': data})


def SelectAllUsers(request):
    if(request.method == "GET"):
        data = list(Users.objects.values())
    return JsonResponse({'data': data})
