from django.shortcuts import render
from django.views import View
# Create your views here.


class homeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')

class productView(View):
    def get(self, request):
        return render(request, 'product/product.html')

class cartView(View):
    def get(self, request):
        return render(request, 'cart/cart.html')

class checkoutView(View):
    def get(self, request):
        return render(request, 'checkout/checkout.html')