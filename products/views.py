from django.shortcuts import render
from django.http import JsonResponse
import http
from django.db.models import Q
import time
from datetime import datetime
import random
from django.shortcuts import redirect
from products.models import Products, Reservations
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def products(request):
    context = {}
    products_instance = Products.objects.all()
    context['products_instance'] = products_instance
    return render(request, 'products.html', context)

def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category_name = request.POST.get('category_name')
        price = request.POST.get('price')
        print('Categories: ',category_name)
        try:
            product_obj = Products()
            product_obj.product_name = product_name
            product_obj.category = category_name
            product_obj.price = price
            product_obj.save()

        except Exception as e:
            print('Exception Error! ',e)

    context = {}
    return render(request, 'add-products.html', context)

def feedback(request):
    context = {}
    return render(request, 'feedback.html', context)

@login_required
def reservations(request, pk):
    context = {
        'reservations'  :   Reservations.objects.filter(user_id=pk, check_in=False)
    }
    return render(request, 'reservations.html', context)

@login_required
def cancelreservations(request, pk):
    reservation_obj = Reservations.objects.get(pk=pk)
    reservation_obj.delete()
    return redirect('index')


@login_required
def makereservation(request):
    context = {}
    context['reserved'] = False
    if request.method == 'POST':
        number_of_guests = request.POST.get('number_of_guests')
        reservation_date = request.POST.get('reservation_date')
        reservation_time = request.POST.get('reservation_time')
        table_number = request.POST.get('table_number')

        print('Number: ',number_of_guests)
        print('table_number: ',table_number)
        print('reservation_date: ',reservation_date)
        print('reservation_time: ',reservation_time)
        

        date = str(reservation_date) + ' ' + str(reservation_time)
        date =datetime.strptime(date, '%Y-%m-%d %H:%M')

        print('reservation_time: ',date)
        
        reservation_obj, created = Reservations.objects.get_or_create(user=request.user, reservation_date=date, table_number=table_number, reserved=True, check_in=False)
        if created:
            print('Reserved')
            reservation_obj.number_of_guests = number_of_guests
            reservation_obj.table_number = table_number
            reservation_obj.save()
            return redirect('index')

        else:
            print('Reservation exist')
            print(reservation_obj)
            context['reserved'] = True
    
    return render(request, 'make_reservation.html', context)

# Sign Up View
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    success_message = "User registered successfuly"
    template_name = 'register.html'

class UserLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, 'Login completed')
        return reverse_lazy('index')

def logout(request):
     del request.session['user_id']
     return redirect('/index')


