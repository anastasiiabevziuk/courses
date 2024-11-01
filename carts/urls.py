from django.urls import path
from . import views


urlpatterns = [
    path("cart_add/<int:course_id>/", views.cart_add, name="cart_add"),
    path("cart_remove/<int:cart_id>/", views.cart_remove, name="cart_remove"),
]
