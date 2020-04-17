from django.urls import path
from .views import view_product, all_products


urlpatterns = [
    path('', all_products, name="all_products"),
    path('<int:pk>/', view_product, name="view_product"),
]
