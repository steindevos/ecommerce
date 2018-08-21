from django.shortcuts import render, redirect

# Create your views here.
def add_to_cart(request):
    product_id = request.POST['id']
    quantity = int(request.POST['quantity'])
    
    cart = request.session.get('cart', {})
    cart[product_id]= cart.get(product_id, 0) + quantity
    
    request.session['cart'] = cart
    print("-------------------------------------------------------")
    print(cart)
    return redirect('show_products')
    
def show_my_cart(request):
    return render(request, "cart/mycart.html")