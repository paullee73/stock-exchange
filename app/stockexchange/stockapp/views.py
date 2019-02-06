from django.shortcuts import render
from stockapp.models import User
from stockapp.models import Stock
from stockapp.forms import CreateForm
from django.http import JsonResponse

# Create your views here
def create_user(request):
	username='invalid form'
	password=''
	balance=''
	if request.method == "POST":
		MyForm = CreateForm(request.POST)
		if MyForm.is_valid():
			username = MyForm.cleaned_data['username']
			password = MyForm.cleaned_data['password']
			balance = MyForm.cleaned_data['balance']
			m_user = User(username = username, password = password, balance = balance)
			m_user.save()
		else:
			MyForm = CreateForm()
	return render(request, 'JSONresponse.html', {'username': username, 'password': password, 'balance': balance})