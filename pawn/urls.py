from django.urls import path
from .views import PawnTransactionListView, PawnTransactionCreateView, Home, CustomerCreateView, ItemCreateView, CustomerListView, ItemListView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('transaction/', PawnTransactionListView.as_view(), name='transaction_list'),
    path('create/', PawnTransactionCreateView.as_view(), name='transaction_create'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('item/create/', ItemCreateView.as_view(), name='item_create'),
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('items/', ItemListView.as_view(), name='item_list'),
]

