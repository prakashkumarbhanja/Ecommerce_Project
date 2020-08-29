from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from products.models import Product
from .models import Cart, CartItem
# Create your views here.

# class Cart_List(ListView): #26
#     model = Cart
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cart = Cart.objects.all()[0]
#         context['cart'] = cart
#         return context

# def cart_list(request):
#     try:
#         the_id = request.session['cart_id']
#     except:
#         the_id = None
#     if the_id:
#         cart = Cart.objects.filter(user=request.user)
#         print(" -------Cart--- ", cart)
#         context = {"cart":cart}
#     else:
#         empty_message = "Your Cart is empty, pls keep shoping"
#         context = {"empty": True, "empty_message": empty_message}
#     template = "carts/cart_list.html"
#     return render(request, template, context)


def cart_list(request):

    cart = Cart.objects.filter(user=request.user)

    empty_message = "Your Cart is empty, pls keep shoping"
    context = {'cart':cart ,"empty": True, "empty_message": empty_message}
    template = "carts/cart_list.html"
    return render(request, template, context)


# def add_to_cartt(reuest, slug):
#
#     try:
#         the_id = reuest.session['cart_id']
#     except:
#         cart = Cart()
#         cart.save()
#         the_id = cart.id
#
#     try:
#         product = Product.objects.get(slug=slug)
#     except product.DoesNotExist:
#         print("------ Searched item DoesNotExist ------")
#
#     cart_item, created = CartItem.objects.get_or_create(user=reuest.user, products=product)
#     # cart_all = CartItem.objects.all()
#     print('---------------- Carts item is -------------', cart_item)
#
#     cart = Cart.objects.get(id=the_id)
#
#     print('***********',cart)
#
#     if not cart_item in CartItem.objects.filter(user=reuest.user, products=product):
#     # if CartItem.objects.filter(user__username=reuest.user, products__title=product).exists():
#         print("-------- Product is not available in the Cart --------------")
#         print("---Cart item quantity is----", cart_item.quantity)
#
#     else:
#         print("------- product is available in the cart and need to increment by +1 -------")
#         cart_item.quantity +=1
#         cart_item.save()
#         print("------- Item Quantity increased ----------")
#
#     if not cart_item in cart.items.all():
#         print("------- Nedd to addtocart -------------")
#         cart.items.add(cart_item)
#         quantity = cart_item.quantity
#         price = quantity* cart_item.products.price
#         cart.total = cart_item.products.price
#         cart.user=reuest.user
#         cart.save()
#     else:
#        pass
#
#     return HttpResponseRedirect("/cart/")

def add_to_cart(reuest, slug):

    try:
        the_id = reuest.session['cart_id']
    except:
        cart = Cart()
        cart.save()
        the_id = cart.id

    try:
        product = Product.objects.get(slug=slug)
    except product.DoesNotExist:
        print("------ Searched item DoesNotExist ------")

    cart_item, created = CartItem.objects.get_or_create(user=reuest.user, products=product)
    # cart_all = CartItem.objects.all()
    print('---------------- Carts item is -------------', cart_item)

    cart = Cart.objects.get(id=the_id)

    print('***********',cart)

    if not cart_item in CartItem.objects.filter(user=reuest.user, products=product):
    # if CartItem.objects.filter(user__username=reuest.user, products__title=product).exists():
        print("-------- Product is not available in the Cart --------------")
        print("---Cart item quantity is----", cart_item.quantity)

    else:
        print("------- product is available in the cart and need to increment by +1 -------")
        cart_item.quantity +=1
        cart_item.save()
        print("------- Item Quantity increased ----------")

    if Cart.objects.filter(user__username=reuest.user).filter(items__products__title=cart_item).exists():

        print("-------- Item has already added to the cart --------")
    else:
        cart.items.add(cart_item)
        quantity = cart_item.quantity
        price = quantity * cart_item.products.price
        cart.total = price
        cart.user=reuest.user
        cart.save()

    return HttpResponseRedirect("/cart/")


def remove_from_cart(request):
    pass