from django.urls import path
from .views import add_to_cart, show_my_cart

urlpatterns = [
    path('add/', add_to_cart, name="add_to_cart"),
    path('mycart', show_my_cart, name="show_my_cart")
]