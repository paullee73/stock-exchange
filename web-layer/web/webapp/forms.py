from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter password'}))


class StockForm(forms.Form):
    ticker = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter stock symbol'}))


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Search'}))
