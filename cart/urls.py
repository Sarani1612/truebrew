from django.urls import path
from .views import view_cart, add_to_cart


urlpatterns = [
    path('', view_cart, name="cart"),
    path('add/<int:id>/', add_to_cart, name="add_to_cart"),
]
