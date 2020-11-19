from django.db import models
import uuid
from customer.models import Customer

# Create your models here.
class Transaction(models.Model):
    timing = models.DateTimeField(auto_now_add = True)
    amount = models.DecimalField(default = 0,decimal_places = 5, max_digits = 30)
    transaction_id = models.UUIDField(default = uuid.uuid4,primary_key = True, editable = False)
    sender = models.ForeignKey(Customer,on_delete = models.CASCADE, related_name = "sender")
    receiver = models.ForeignKey(Customer,on_delete = models.CASCADE, related_name = "receiver")