from django import forms
from django.forms import ModelForm, widgets
from userprofile.models import Transactions, Bills


class TransactionForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ["tr_type", "amount", "bill"]


class BillForm(ModelForm):


    class Meta:
        model = Bills
        fields = ["bill_name", "balance", "descript"]
        widgets = {
            "bill_name": forms.TextInput(attrs={
                "placeholder": "Название счета:", 
                "class": "form-control"
            }),
            "balance": forms.NumberInput(attrs={
                "placeholder": "Начальный баланс:", 
                "class": "form-control"
            }),
            "descript": forms.Textarea(attrs={
                "placeholder": "Описание счета:", 
                "class": "form-control"
            }),
        }
