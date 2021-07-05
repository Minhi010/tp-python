from django.urls import path

from . import views

app_name='products'

urlpatterns = [
     path('search', views.ProductSearchListView.as_view(), name='search'),
     path('<slug:slug>', views.ProductDetailView.as_view(), name='product'), #id -> llave primaria 
     path('nuevo/', views.new, name='new'),
     path('<slug:slug>/editar', views.edit, name='edit'),
     path('<slug:slug>/borrar', views.delete, name='delete'),
]
