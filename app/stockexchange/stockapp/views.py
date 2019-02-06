from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from .models import User, Stock
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return HttpResponse("Test")


def CreateUser(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        balance = request.POST['balance']
        if(len(username) == 0 or len(password) == 0 or not balance.isdigit()):
        	return JsonResponse({'ERROR': 'Invalid input'})

        newUser = User(username = username, password=password, balance=float(balance))
        newUser.save()

        return JsonResponse({'username': username, 'password': password, 'balance': balance})


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
		user = None
		ticker = request.POST['ticker']
		user_id = request.POST['user_id']
		if(len(ticker) == 0 or len(user_id) == 0):
			return JsonResponse({'ERROR': 'Invalid input'})
		try:
			user = User.objects.get(pk=user_id)
		except ObjectDoesNotExist:
			return JsonResponse({'ERROR': 'User with that ID does not exist'})
		newStock = Stock(ticker_sym = ticker, user=user)
		newStock.save()
		return JsonResponse({'ticker symbol': ticker, 'owner': user_id})

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