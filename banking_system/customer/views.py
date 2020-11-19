from django.shortcuts import render,get_object_or_404,redirect
from .models import Customer
from django.views.generic import ListView
from .forms import MoneyTransferForm
from django.contrib import messages
from transaction.models import Transaction

# Create your views here.
def welcome(request):
	# change the template
	return render(request,"customer/welcome.html")

class CustomerListView(ListView):
	model = Customer
	template_name = 'customer/home.html'
	context_object_name = 'customer_list'
	ordering = ['-date_created','name']
	paginate_by = 5

def Profile(request,id):
	obj = get_object_or_404(Customer,account_number = id)
	context = {"object": obj}
	return render(request,"customer/details.html",context)

class Debtor(ListView):
	model = Customer
	template_name = 'transaction/debtor_selection.html'
	context_object_name = 'customer_list'
	ordering = ['-date_created','name']
	paginate_by = 5

def Transfer(request,creditor,debtor):
	creditor_obj = get_object_or_404(Customer,account_number = creditor)
	debtor_obj = get_object_or_404(Customer,account_number = debtor)
	message = ""
	msg_status = ""
	form = MoneyTransferForm(request.POST or None)
	if request.method == "POST":
	    if form.is_valid() and form.sufficient_balance(creditor_obj):
	    	try:
	    	    debtor_obj.balance = debtor_obj.balance + form.cleaned_data.get('money')
	    	    creditor_obj.balance = creditor_obj.balance - form.cleaned_data.get('money')
	    	    debtor_obj.save()
	    	    creditor_obj.save()
	    	    tran = Transaction(amount = form.cleaned_data.get('money'),sender = creditor_obj, receiver = debtor_obj)
	    	    tran.save()
	    	    messages.success(request,f'Amount transferred successfully!!!')
	    	except:
	    	    messages.error(request,f'Transaction Failed!!!')    
	    	return redirect('money-transfer',creditor,debtor)	
	    elif  not form.is_valid():
	        message = "Invalid input"	
	        msg_status = "wrong"
	    else:
	        message = "Insufficient balance" 
	        msg_status = "wrong"   
	context = {"creditor_obj": creditor_obj, "debtor_obj": debtor_obj,"form": form,"transaction_message": message,"msg_status":msg_status}
	return render(request,"transaction/transaction_process.html",context)