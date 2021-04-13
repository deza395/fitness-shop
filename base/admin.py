from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class ProductAdmin( ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields = ['name'] 
    list_display=('user','name','image','brand','category','description','rating','numReviews', 'price', 'countInStock')
    resource_class = ProductResource


# Register your models here.
admin.site.register(Product, ProductAdmin)

admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
