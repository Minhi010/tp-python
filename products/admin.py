from django.contrib import admin
from django.db.models import fields
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):#modificar el comportamiento del producto en admin 
    fields = ('title', 'description', 'price', 'image')
    list_display = ('__str__','slug', 'created_at')

admin.site.register(Product, ProductAdmin)