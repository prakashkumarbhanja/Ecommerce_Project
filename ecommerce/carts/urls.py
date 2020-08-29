from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_list, name='cart'),
    path('add-to-cart/<slug>', add_to_cart, name='add_to_cart'),
]