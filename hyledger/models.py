from django.db import models

# Create your models here.


class Clients(models.Model):
	name = models.CharField(max_length=200)
	balance = models.IntegerField(default=0)
	phone = models.IntegerField(null=True)
	firm_name = models.CharField(max_length=255, null=True)
	email = models.EmailField(null=True)

	def __str__(self):
		return self.name


class Transaction(models.Model):
	name = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True)
	transaction_type = models.CharField(max_length=200)
	amount = models.IntegerField()
	date= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name.name