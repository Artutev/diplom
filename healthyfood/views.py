from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from healthyfood.models import ProductCategory, Product, Basket
from users.models import User

# Create your views here.

def index(request):
    context = {
        'title': 'Healthy Food',
    }
    return render(request, 'healthyfood/index.html', context)

def menu(request):
    context = {
        'title': 'Меню',
        'menu': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'healthyfood/menu.html',context)

@login_required()
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
