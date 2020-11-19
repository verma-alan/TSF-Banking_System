from django.shortcuts import render
from .models import Transaction
from django.views.generic import ListView

# Create your views here.
class TransactionListView(ListView):
	model = Transaction
	template_name = "transaction/home.html"
	context_object_name = 'transaction_list'
	ordering  = ['-timing','amount']
	paginate_by = 5