from django.contrib import admin
from store.models import WholesaleItem

# Register your models here.
class WholesaleItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage_form', 'brand', 'unit', 'cost', 'price', 'stock', 'low_stock_threshold', 'exp_date', 'markup')
    search_fields = ('name',)
    fields_editable = ('low_stock_threshold',)
    list_filter = ('markup', 'unit', 'exp_date')




















admin.site.register(WholesaleItem, WholesaleItemAdmin)