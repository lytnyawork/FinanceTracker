from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView

from userprofile.forms import TransactionForm
from userprofile.models import Bills, Transactions





