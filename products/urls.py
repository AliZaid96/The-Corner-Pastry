from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('product', views.products, name='products'),
    path('add-products', views.add_product, name='add_product'),
    path('feedback', views.feedback, name='feedback'),
    path('make-reservation/', views.makereservation, name='make_reservation'),

    path('reservations/<int:pk>', views.reservations, name='reservations'),
    path('cancel-reservations/<str:pk>', views.cancelreservations, name='cancel-reservation'),

    path('login', views.UserLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),
]
