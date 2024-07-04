from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Customer, Item, PawnTransaction
from .forms import PawnTransactionForm, CustomerForm, ItemForm

class PawnTransactionListView(View):
    def get(self, request):
        transactions = PawnTransaction.objects.all()
        return render(request, 'pawn/transaction_list.html', {'transactions': transactions})

class PawnTransactionCreateView(View):
    def get(self, request):
        form = PawnTransactionForm()
        return render(request, 'pawn/transaction_form.html', {'form': form})

    def post(self, request):
        form = PawnTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
        return render(request, 'pawn/transaction_form.html', {'form': form})

class Home(View):    
    def get(self, request):
        return render(request, "pawn/base.html")
    

class CustomerCreateView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'pawn/customer_form.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'pawn/customer_form.html', {'form': form})

class ItemCreateView(View):
    def get(self, request):
        form = ItemForm()
        return render(request, 'pawn/item_form.html', {'form': form})

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        return render(request, 'pawn/item_form.html', {'form': form})
    

class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'pawn/customer_list.html', {'customers': customers})

class ItemListView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'pawn/item_list.html', {'items': items})
