from django.contrib import admin
from .models import User, Categories, Products, WebsiteUser, CustomerOrder

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(WebsiteUser)
admin.site.register(CustomerOrder)


