from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from .models import User
from django.urls import reverse

def index(request):
    return HttpResponse("Test")


def createUser(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        balance = float(request.POST['balance'])
        newUser = User(username = username, password=password, balance=balance)
        newUser.save()

        return JsonResponse({'username': username, 'password': password, 'balance': balance})


def ViewOrUpdateUser(request, uniqueID):
    if(request.method == "GET"):
        return JsonResponse(serializers.serialize("json", [User.objects.get(pk=uniqueID),]), safe=False )
    if(request.method == "POST"):
        userToUpdate = User.objects.get(pk=uniqueID)
        username = request.POST['username']
        password = request.POST['password']
        balance = request.POST['balance']

        if(username):
            userToUpdate.username = username
        if(password):
            userToUpdate.password = password
        if(balance):
        	userToUpdate.balance = balance
        
        userToUpdate.save()
        
        return JsonResponse(serializers.serialize("json", [userToUpdate]), safe = False)


def DeleteUser(request, uniqueID):
    if(request.method == "POST"):
    	userToDelete = User.objects.get(pk=uniqueID)
    	username = userToDelete.username
    	password = userToDelete.password
    	balance = userToDelete.balance
    	userToDelete.delete()
    	return JsonResponse({'username': username, 'password': password, 'balance': balance})