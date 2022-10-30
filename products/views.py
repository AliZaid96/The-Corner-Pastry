from django.shortcuts import render
from django.http import JsonResponse
import http
from django.db.models import Q
import time
import random
from django.shortcuts import redirect
from products.models import Categories, WebsiteUser, CustomerOrder, Products
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib import messages
from .forms import SignUpForm

def products(request):
    context = {}
    products_instance = Products.objects.all()
    context['products_instance'] = products_instance
    return render(request, 'products.html', context)

def customer_order(request):
      context = {}
      customer_instance = CustomerOrder.objects.all()
      context['customer_instance'] = customer_instance
      return render(request, 'customer-order.html', context)

def category(request):
    context = {}
    category_instance = Categories.objects.all()
    context['category_Date'] = category_instance
    return render(request, 'categories.html', context)

def add_category(request):
    context = {}
    return render(request, 'add-category.html', context)

def add_product(request):
    context = {}
    category_instance = Categories.objects.all()
    context['category_Date'] = category_instance
    return render(request, 'add-products.html', context)

def feedback(request):
    context = {}
    return render(request, 'feedback.html', context)

def order_details(request):
    context = {}
    product_id = request.GET.get('product_id')
    user_id = request.session['user_id']
    current_date = time.strftime('%Y-%m-%d')
    random_number = random.randint(100000, 999999)

    user_get_count = CustomerOrder.objects.filter(product_id=product_id, order_date=current_date).count()
    if user_get_count == 0:
        order_obj = CustomerOrder()
        order_obj.website_customer_id = user_id
        order_obj.product_id = product_id
        order_obj.order_date = current_date
        order_obj.save()

    return_data = []
    data = Products.objects.raw(
        'SELECT c.* , (select product_name from  products where id = c.product_id ) as product_name , (select id from  products where id = c.product_id ) as p_id , (select price from  products where id = c.product_id ) as product_price  , (select id from  website_user where id = c.website_customer_id ) as customer_id FROM customer_order c')
    for p in data:
        product_name = p.product_name
        price = p.product_price
        p_id = p.p_id
        customer_id = p.customer_id
        status = p.status
        sum_amount= p.sum_amount
        quantity= p.quantity
        obj = {
            'product_name': product_name,
            'price': price,
            'p_id': p_id,
            'customer_id': customer_id,
            'status': status,
            'sum_amount': sum_amount,
            'quantity': quantity
        }
        return_data.append(
            obj
        )
    context['return_data'] = return_data
    context['user_id'] = user_id
    return render(request, 'order-details.html', context)

def order_now_ajax(request):
        context = {}
        print("working")
        return_array = []
        quantity = request.POST.getlist("quantity[]")
        product_id = request.POST.getlist("product_id[]")
        sum_amount = request.POST.getlist("sum_amount[]")
        is_many = isinstance(request.data, list)
        print(is_many)
        return JsonResponse(context, status=http.HTTPStatus.OK)

def indiviual_order(request):
    context = {}
    product_id = request.GET.get("product_id")
    customer_id = request.GET.get("customer_id")
    quantity = request.GET.get('quantity')
    sum_amount = request.GET.get('sum_amount')
    print('Product ID: ',product_id)

    objects = CustomerOrder.objects.filter(product_id=product_id, website_customer_id=customer_id)
    print('Object: ',objects)
    for obj in objects:
        print('Inside For loop ',obj)
        obj.quantity = quantity
        obj.sum_amount = sum_amount
        obj.status = 1
        obj.save()

    context['status'] = 1                                  
    return JsonResponse(context, status=http.HTTPStatus.OK)

def category_ajax(request):
    context = {}
    category_name = request.GET.get('category_name')
    try:
        category_boj = Categories()
        category_boj.name = category_name
        category_boj.save()
        context['status'] = 1
        context['developer_message'] = "Category added successfully"
    except Exception as e:
        context['status'] = -2
        context['developer_message'] = "Something went wrong"
    return JsonResponse(context, status=http.HTTPStatus.OK)

def add_product_ajax(request):
    context = {}
    product_name = request.POST.get('product_name')
    category_name = request.POST.get('category_name')
    price = request.POST.get('price')
    print('Categories: ',category_name)

    if request.method == 'POST':
        try:
            category_name = Categories.objects.get(name=category_name)
            print('Obj: ',category_name)
            product_obj = Products()
            product_obj.product_name = product_name
            product_obj.category_id = category_name.pk
            product_obj.price = price
            product_obj.save()
            context['status'] = 1
            context['developer_message'] = "Product added successfully"
        except Exception as e:
            print('Exception Error! ',e)
            context['status'] = -2
            context['developer_message'] = "Something went wrong"
    return JsonResponse(context, status=http.HTTPStatus.OK)

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


