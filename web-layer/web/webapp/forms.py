from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter password'}))
