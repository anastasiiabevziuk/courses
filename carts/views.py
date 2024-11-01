from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from carts.models import Cart
from carts.utils import get_user_carts

from shop.models import Course


def cart_add(request, course_id):

    course = Course.objects.get(pk=course_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(title=course.title, user=request.user)
        is_duplicate = carts.exists()
        cart = carts.first()
        if is_duplicate:
            cart.quantity += 1
            cart.save()

        else:
            Cart.objects.create(
                title=course.title,
                price=course.price,
                quantity=1,
                user=request.user,
            )
    else:
        carts = Cart.objects.filter(
            title=course.title, session_key=request.session.session_key
        )
        is_duplicate = carts.exists()
        cart = carts.first()
        if is_duplicate:
            cart.quantity += 1
            cart.save()

        else:
            Cart.objects.create(
                title=course.title,
                price=course.price,
                quantity=1,
                session_key=request.session.session_key,
            )

    return redirect("user-cart")


def cart_remove(request, cart_id):

    user_cart = get_user_carts(request)
    cart = user_cart.get(id=cart_id)
    cart.delete()

    return redirect(request.META["HTTP_REFERER"])
