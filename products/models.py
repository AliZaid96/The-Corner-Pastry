from django.db import models
from django.db import models
from django.contrib.auth.models import User
import uuid

categories = [
    ('pz', 'Pizza'),
    ('sp', 'Spaghetti'),
    ('sw', 'Sweets'),
]

class Products(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=2, choices=categories)
    price = models.IntegerField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Products'


class Reservations(models.Model):
    reservation_id = models.CharField(max_length=40, primary_key=True, unique=True, default=uuid.uuid4, verbose_name = 'Order #')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_order')
    reservation_date = models.DateTimeField()
    number_of_guests = models.IntegerField(null=True, blank=True)
    reserved = models.BooleanField(default=True)
    check_in = models.BooleanField(default=False)
    table_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.reservation_id

    class Meta:
        verbose_name_plural = 'Reservations'