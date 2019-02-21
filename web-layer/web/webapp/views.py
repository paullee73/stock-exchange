from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
import urllib.request
import urllib.parse
import urllib.error
import json

# Create your views here.
def index(request):
    return HttpResponse("Test")

def displayStocks(request):
	if (request.method == 'GET'):
		req = urllib.request.Request("http://exp-api:8000/exp/stock/item_detail")
		resp_json = urllib.request.urlopen(req).read().decode('utf-8')
		resp = json.loads(resp_json)
		resplist = resp['data']
	return render(request, 'item_detail.html', {'resplist' : resplist})

def userDetail(request, uniqueID):
	if (request.method == 'GET'):
		req = urllib.request.Request("http://exp-api:8000/exp/user/" + uniqueID + "")
		resp_json = urllib.request.urlopen(req).read().decode('utf-8')
		resp = json.loads(resp_json)
	#return JsonResponse({'resp' : resp})
	return render(request, 'user_detail.html', {'resp' : resp})