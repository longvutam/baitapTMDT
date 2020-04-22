from django.urls import path
from .views import homeView,productView,cartView,checkoutView

urlpatterns = [
    path('', homeView.as_view(), name = 'index'),
    path('product/', productView.as_view(), name = 'product'),
    path('cart/', cartView.as_view(), name = 'cart'),
    path('checkout/', checkoutView.as_view(), name = 'checkout')
]