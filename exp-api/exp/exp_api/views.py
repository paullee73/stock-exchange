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

def StockAll(request):
	if (request.method == 'GET'):
		resp = {}
		try:
			req = urllib.request.Request('http://models-api:8000/stockapp/stock/item_detail')
			resp_json = urllib.request.urlopen(req).read().decode('utf-8')
			resp = json.loads(resp_json)['items']
		except urllib.error.URLError as e:
			print(e.reason)
	return JsonResponse({'items': resp})


