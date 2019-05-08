from django import forms

class CreateForm(forms.Form):
	username = forms.CharField(max_length = 30)
	password = forms.CharField(max_length = 30)
	balance = forms.DecimalField(max_digits = 50, decimal_places = 2)
