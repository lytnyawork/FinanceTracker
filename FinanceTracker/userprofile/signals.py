from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transactions

@receiver([post_save, post_delete], sender=Transactions)
def update_bill_balance(sender, instance, **kwargs):
    instance.bill.update_balance()