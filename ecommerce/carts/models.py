from django.db import models

from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
class CartItem(models.Model):
    # cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True, blank=True)
    products = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantity = models.IntegerField( default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.products.title

    @property
    def total_price(self):
        self.quantity * self.products.price


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(CartItem, null=True, blank=True)
    # product = models.ManyToManyField(Product, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Cart id: %s' %(self.id)

    @property
    def product_count(self):
        return self.product.count()