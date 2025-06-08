from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms import CharField

# Create your models here

class Wallet(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_balance = models.DecimalField(max_digits=12, default=0, decimal_places=2)


    @receiver([post_save], sender=User)
    def create_user_wallet(sender, instance, created, **kwargs):
        if created:
            Wallet.objects.create(user=instance)
        


    def update_total_balance(self):
        self.total_balance = sum(wallet.balance for wallet in self.wallets.all())
        self.save()




class Bills(models.Model):

    bill_name = models.CharField(max_length=100)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallets')
    balance = models.DecimalField(max_digits=12, default=0, decimal_places=2)
    descript = models.TextField(default='')

    def update_balance(self):
        total_plus = self.transactions.filter(tr_type='plus').aggregate(
        total=models.Sum('amount')
        )['total'] or 0
        total_minus = self.transactions.filter(tr_type='minus').aggregate(
        total=models.Sum('amount')
        )['total'] or 0

        self.balance = total_plus - total_minus
        if self.balance < 0:
            self.balance = 0  # Исправлено "==" на "="

        self.save() 
        self.wallet.update_total_balance()


class Transactions(models.Model):
    TYPE = (
        ('plus', 'Поступление'),
        ('minus', 'Отступление')
    )
    tr_type = models.CharField(max_length=5, choices=TYPE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    bill = models.ForeignKey(Bills, on_delete=models.CASCADE, related_name='transactions')
    created_at = models.DateTimeField(auto_now_add=True)