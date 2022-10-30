from django.contrib import admin
from .models import Categories, Products, CustomerOrder, OrderProducts

class CategoriesTableView(admin.ModelAdmin):
	list_display = ('id', 'name')
	search_list = ['name']

class ProductsTableView(admin.ModelAdmin):
	list_display = ('id', 'product_name', 'price', 'category')
	search_list = ['product_name']
	filter_list = ['category']

class CustomerOrderTableView(admin.ModelAdmin):
	list_display = ('order_id', 'user', 'order_date', 'total_amount', 'active')
	search_list = ['order_id']
	filter_list = ['active', 'order_date']

class OrderProductsTableView(admin.ModelAdmin):
	list_display = ('pk', 'order_id', 'product', 'quantity', 'sub_total')
	search_list = ['order_id']
	filter_list = ['active', 'order_date']

admin.site.register(Categories, CategoriesTableView)
admin.site.register(Products, ProductsTableView)
admin.site.register(CustomerOrder, CustomerOrderTableView)
admin.site.register(OrderProducts, OrderProductsTableView)