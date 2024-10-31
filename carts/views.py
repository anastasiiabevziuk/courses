from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from carts.models import Cart

from shop.models import Course


def cart_add(request, course_id):

    course = Course.objects.get(pk=course_id)
    carts = Cart.objects.filter(title=course.title)
    is_duplicate = carts.exists()
    cart=carts.first()
  
    if is_duplicate:

        cart.quantity +=1
        cart.save()
 
    else:
        Cart.objects.create(title=course.title, price= course.price, quantity=1 )
 
    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])
    
