from django.db import models

class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	balance = models.DecimalField(max_digits= 30, decimal_places = 2)

class Stock(models.Model):
	ticker_sym = models.CharField(max_length=5)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


