from .models import Cart

def get_or_create_cart(request):
    #elimina la sesion    request.session['cart_id']=None
    user = request.user if request.user.is_authenticated else None
    #obtenemos el user autenticado y generamos el carrito
    cart_id = request.session.get('cart_id')#retorna none si la llave no existe
    cart=Cart.objects.filter(cart_id=cart_id).first() #[] sino encuentra devuelve none
    #crear y obtener carrito usando el valor none
    if cart is None:
        cart = Cart.objects.create(user=user)
    if user and cart.user is None:
        cart.user=user
        cart.save()

    request.session['cart_id'] = cart.cart_id
    
    return cart