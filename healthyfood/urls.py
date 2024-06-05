from django.urls import path

from healthyfood.views import menu, basket_add, basket_remove

app_name = 'healthyfood'

urlpatterns = [
    path('', menu, name='index'),
    path('baskets/add/<int:product_id>', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>', basket_remove, name='basket_remove'),
]
