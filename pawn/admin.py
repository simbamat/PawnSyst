from django.contrib import admin
from .models import Customer, Item, PawnTransaction

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(PawnTransaction)