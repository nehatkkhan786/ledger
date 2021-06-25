from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Clients, Transaction
# Create your views here.


class HomepageView(View):
	def get(self, request, *args, **kwargs):
		clients = Clients.objects.all()
		return render(request, 'homepage.html', {'clients':clients})

class ClientDetailView(View):
	def get(self, request, pk,  *args, **kwargs):
		client = get_object_or_404(Clients, pk=pk)
		client_transaction = Transaction.objects.filter(name=client)
		total_transactions = client_transaction.count()

		return render(request, 'client_detail.html', {'client':client, 'client_transaction':client_transaction, 'total_transactions':total_transactions})

def CreditView(request, pk):
	client = get_object_or_404(Clients, pk=pk)
	if request.method == 'POST':

		amount = request.POST.get('amount')
		amount = int(amount)
		client.balance += amount
		client.save()
		transaction = Transaction.objects.create(
			name=client,
			transaction_type = 'CREDIT', 
			amount = amount,
			)
		transaction.save()
		return redirect('home')

def DebitView(request, pk):
	client = get_object_or_404(Clients, pk=pk)
	if request.method == 'POST':

		amount = request.POST.get('amount')
		amount = int(amount)
		client.balance -= amount
		client.save()
		transaction = Transaction.objects.create(
			name=client,
			transaction_type = 'DEBIT', 
			amount = amount,
			)
		transaction.save()
		return redirect('home')



def create_client(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		firm_name = request.POST.get('firm_name')
		form = Clients.objects.create(name=name, email=email, phone=phone, firm_name=firm_name)
		form.save()
		return redirect('home')
