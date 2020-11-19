from django import forms

class MoneyTransferForm(forms.Form):
	money = forms.DecimalField(max_digits = 30)

	def sufficient_balance(self,obj,*args,**kwargs):
		money = self.cleaned_data.get('money')
		if self.is_valid():
		    if  money > obj.balance:
			    return False
		else:
		    return False	    
		return True	