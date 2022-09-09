from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    dob = models.CharField(max_length=2500, null=True)
    email = models.CharField(max_length=250, blank=True, null=True, unique=False)
    REQUIRED_FIELDS = ['email', 'password', 'name']

    class Meta:
        db_table = 'user'


class Categories(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'category'


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()

    class Meta:
        db_table = 'products'


class WebsiteUser(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    REQUIRED_FIELDS = ['email', 'password', 'customer_name']

    class Meta:
        db_table = 'website_user'


class CustomerOrder(models.Model):
    website_customer = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE, null=True, related_name='cats')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, related_name='product')
    order_date = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    sum_amount = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(null=True, default=0)


    class Meta:
        db_table = 'customer_order'




