from django import forms
from .models import PawnTransaction, Customer, Item

class PawnTransactionForm(forms.ModelForm):
    class Meta:
        model = PawnTransaction
        fields = ['customer', 'item', 'amount_loaned', 'pawn_date', 'pawn_renewal_date', 'pawn_expiry_date']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'value']