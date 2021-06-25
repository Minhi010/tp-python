from categories.models import Category
from django.shortcuts import render

from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

# Create your views here.
class ProductListView(ListView):
    template_name='index.html'
    queryset=Product.objects.all().order_by('-id')
    
    def  get_context_data(self, **kwargs):#pasa el modelo de la clase al template
            context= super().get_context_data(**kwargs)
            context['message']='Listado de productos'
            
            return context
 

class ProductDetailView(DetailView): #busqueda mediante id -> pk
    model = Product
    template_name='products/product.html'

   

class ProductSearchListView(ListView):
   template_name='products/search.html' 

   def get_queryset(self):
       #SELECT *FROM products WHERE title like %valor%
       #donde la i indica que no es sensible a las mayus
       filters= Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
       return Product.objects.filter(filters)

   def query(self):
       return self.request.GET.get('q')
    
   def  get_context_data(self, **kwargs):#pasa el modelo de la clase al template
            context= super().get_context_data(**kwargs)
            context['query'] = self.query()
            context['count'] = context['product_list'].count()

            return context