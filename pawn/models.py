from django.db import models
from django.utils import timezone
from datetime import timedelta

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class PawnTransaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    pawn_date = models.DateTimeField(default=timezone.now)
    pawn_renewal_date = models.DateTimeField(null=True, blank=True)
    pawn_expiry_date = models.DateTimeField(default=timezone.now() + timedelta(days=30))
    amount_loaned = models.DecimalField(max_digits=10, decimal_places=2)
    redeemed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer} pawned {self.item}"
