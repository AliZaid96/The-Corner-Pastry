from django.shortcuts import render
from products.models import Products
from django.db.models import Q

def index(request):
    print('Index')
    context = {
        'user_id'   :   request.user.pk,
        'pizzas'  :   Products.objects.filter(category='pz'),
        'spaghetties'  :   Products.objects.filter(category='sp'),
        'sweets'  :   Products.objects.filter(category='sw'),

    }
    return render(request, 'index.html', context)


def index_admin(request):
    context = {
        'products'  :   Products.objects.all()
    }
    return render(request, 'admin-index.html', context)
