

from django.urls import path
from . import views

urlpatterns = [
    path('product', views.products, name='products'),
    path('category', views.category, name='category'),
    path('add-category', views.add_category, name='add_category'),
    path('add-products', views.add_product, name='add_product'),
    path('login', views.login, name='login'),
    path('feedback', views.feedback, name='feedback'),
    path('signup', views.signup, name='signup'),
    path('order-details', views.order_details, name='order_details'),
    path('category_ajax/', views.category_ajax, name='category_ajax'),
    path('add_product_ajax/', views.add_product_ajax, name='add_product_ajax'),
    path('login_ajax/', views.login_ajax, name='login_ajax'),
    path('signup_ajax/', views.signup_ajax, name='signup_ajax'),
    path('order_now_ajax/', views.order_now_ajax, name='order_now_ajax'),
    path('indiviual_order/', views.indiviual_order, name='indiviual_order'),
    path('customer_order', views.customer_order, name='customer_order'),
    path('logout/', views.logout, name='logout'),





]
