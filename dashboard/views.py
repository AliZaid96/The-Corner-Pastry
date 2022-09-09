from django.shortcuts import render
from products.models import Categories, Products
from django.db.models import Q
# Create your views here.


def index(request):
    context = {}
    user_id = 0
    category_array = []
    category_1_data = Products.objects.filter(category_id=1)
    category_2_data = Products.objects.filter(category_id=2)
    category_3_data = Products.objects.filter(category_id=3)

    if 'user_id' in request.session:
        user_id = request.session['user_id']

    context['category_1_data'] = category_1_data
    context['category_2_data'] = category_2_data
    context['category_3_data'] = category_3_data
    context['user_id'] = user_id

    return render(request, 'index.html', context)


def index_admin(request):
    context = {}
    return render(request, 'admin-index.html', context)
