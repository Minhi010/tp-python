from django.http.response import HttpResponseRedirect
from tienda.forms import RegisterForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from categories.models import Category
# from django.contrib.auth.models import User
from users.models import User
from .forms import RegisterForm
from products.models import Product
from django.contrib.auth.decorators import user_passes_test

# def index(request):
#     #recibe 3 arg, la peticion, el archivo a render y un contexto(dicc)
#     products=Product.objects.all().order_by('-id')

#     return render (request, 'index.html', { 
#         'message': 'Listado de productos',
#         'title': 'Productos',
#         'products':products,
#     })

#autenticar y generar una sesion para usuario
def login_view (request):
       if request.user.is_authenticated:
            return redirect ('index')
       if request.method =='POST':
           username = request.POST.get ('username') #DICCIONARIO
           password = request.POST.get ('password') #si no encuentra da none

           user = authenticate(username=username, password=password)#none
           
           if user:
               login(request, user)
               messages.success(request,'Bienvenido {}'.format(user.username))
               
               if request.GET.get('next'):
                   return HttpResponseRedirect(request.GET['next'])
               return redirect('index')
           else:
               messages.error(request, 'Usuario o contraseña no validos')

       return render (request, 'users/login.html', {

       })

def logout_view (request):

    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')    
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
    return render(request, 'users/register.html',{
        'form': form,
        'title': 'Registro'
    })

def about(request):
    return render(request, 'about.html',{
    'title': '¿Quienes somos?'
})