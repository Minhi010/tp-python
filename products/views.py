from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

# Create your views here.
class ProductListView(ListView):
    template_name='index.html'
    queryset=Product.objects.all().order_by('-id')

 

class ProductDetailView(DetailView): #busqueda mediante id -> pk
    model = Product
    template_name='products/product.html'

    def  get_context_data(self, **kwargs):#pasa el modelo de la clase al template
        context= super().get_context_data(**kwargs)
        
        print(context)
        
        return context