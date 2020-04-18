from django.urls import path
from .views import view_cart, add_to_cart, adjust_quantity, delete_subscription


urlpatterns = [
    path('', view_cart, name="cart"),
    path('add/<id>/', add_to_cart, name="add_to_cart"),
    path('adjust/<id>/', adjust_quantity, name="adjust_quantity"),
    path('delete/<id>/', delete_subscription, name="delete_subscription"),
]
