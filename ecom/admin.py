
from django.contrib import admin
from ecom.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_pro', 'price_pro', 'description')
    search_fields = ('name_pro',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('firstname_user', 'lastname_user', 'phone_user')
    search_fields = ('lastname_user',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('priceOrder', 'amount')
    search_fields = ('lastname_user',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Transaction, TransactionAdmin)