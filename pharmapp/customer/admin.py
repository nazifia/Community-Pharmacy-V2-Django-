from django.contrib import admin
from .models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'user')
    search_fields = ('name', 'phone')
    list_filter = ('user',)

class WholesaleCustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'user')
    search_fields = ('name', 'phone')
    list_filter = ('user',)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('customer', 'balance')
    search_fields = ('customer__name',)

class WholesaleCustomerWalletAdmin(admin.ModelAdmin):
    list_display = ('customer', 'balance')
    search_fields = ('customer__name',)












admin.site.register(Customer, CustomerAdmin)
admin.site.register(WholesaleCustomer, WholesaleCustomerAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(WholesaleCustomerWallet, WholesaleCustomerWalletAdmin)