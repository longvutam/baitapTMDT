from django.shortcuts import render
from django.views import View
# Create your views here.


class homeView(View):
    def get(self, request):
        return render(request, 'home.html')

class productView(View):
    def get(self, request):
        return render(request, 'product.html')

class cartView(View):
    def get(self, request):
        return render(request, 'cart.html')

class checkoutView(View):
    def get(self, request):
        return render(request, 'checkout.html')

# def home_view(request):
#     object_list = Page.objects.all().filter()
#     return render(request, 'home.html', {
#         'object_list': object_list,
#         'nav': 'home'
#     })
