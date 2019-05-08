from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(
        attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(label='password', widget=forms.TextInput(
        attrs={'placeholder': 'Enter password'}))


class StockForm(forms.Form):
    ticker = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Stock Symbol'}))
    price = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Price'}))


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Search'}))
