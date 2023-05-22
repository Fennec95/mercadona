from django.contrib import admin
from store.models import Product, Order, Cart
from store.models import Promotion
from django import forms


# Register your models here.
class ProductAdminForm(forms.ModelForm):
    promotion_discount = forms.DecimalField(label='Discount (%)', max_digits=5, decimal_places=1, required=False)

   


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'price', 'promotion')
    list_filter = ('promotion',)
    fields = ('name', 'price', 'promotion', 'promotion_discount')
    search_fields = ('name', 'promotion__name')



admin.site.register(Product)
admin.site.register(Promotion)
admin.site.register(Order)
admin.site.register(Cart)
