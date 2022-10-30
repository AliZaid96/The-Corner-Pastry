from django.db import models
from django.db import models
from django.contrib.auth.models import User
import uuid

class Categories(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Products(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Products'


class CustomerOrder(models.Model):
    order_id = models.CharField(max_length=40, primary_key=True, unique=True, default=uuid.uuid4, verbose_name = 'Order #')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_order')
    order_date = models.DateTimeField(blank=True, null=True)
    total_amount = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name_plural = 'Customer Orders'

class OrderProducts(models.Model):
    order_id = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, null=True, related_name='order')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, related_name='product')
    quantity = models.CharField(max_length=100, blank=True, null=True)
    sub_total = models.IntegerField()

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name_plural = 'Order Products'