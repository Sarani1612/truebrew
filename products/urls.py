from django.urls import path
from .views import view_product


urlpatterns = [
    path('<int:pk>/', view_product, name="view_product"),
]
