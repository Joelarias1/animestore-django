from django.contrib import admin
from .models import Product, category, imageProduct
# Register your models here.


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price')
    list_filter = ('name',)
    
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'typeOf')
    list_filter = ('typeOf',)
    inlines = [ProductInline]
    
    
    


admin.site.register(Product, ProductAdmin)
admin.site.register(category, categoryAdmin)
