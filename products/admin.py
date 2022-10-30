from django.contrib import admin
from .models import Products, Reservations

class ProductsTableView(admin.ModelAdmin):
	list_display = ('id', 'product_name', 'price', 'category')
	search_list = ['product_name']
	filter_list = ['category']

class ReservationsTableView(admin.ModelAdmin):
	list_display = ('reservation_id', 'user', 'reservation_date', 'number_of_guests', 'table_number', 'reserved', 'check_in')
	search_list = ['reservation_id']
	filter_list = ['reserved', 'order_date']

admin.site.register(Products, ProductsTableView)
admin.site.register(Reservations, ReservationsTableView)
