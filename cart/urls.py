from django.urls import path
from .views import view_cart, add_to_cart, adjust_quantity, delete_subscription


urlpatterns = [
    path('', view_cart, name="cart"),
    path('add/<int:id>/', add_to_cart, name="add_to_cart"),
    path('adjust/<int:id>/', adjust_quantity, name="adjust_quantity"),
    path('delete/<int:id>/', delete_subscription, name="delete_subscription"),
]
