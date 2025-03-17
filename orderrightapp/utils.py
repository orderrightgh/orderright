import json
from .models import *


def cookieCart(request):
    try:
        cart  = json.loads(request.COOKIES['cart'])
        print(cart)
    except:
        cart = {}
        print(cart)
    print('Cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
    cartItems =  order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity'] 
            product = Products.objects.get(id = i)
            total = (product.price* cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'product': {
                    'id' : product.id,
                    'name': product.name,
                    'price' : product.price,
                    'imageURL': product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'get_total' : total,
            }
            items.append(item)
            if product.digital == False:
                order['shipping'] = True
        except:
            pass

    return {'items':items, 'order': order, 'cartItems': cartItems}

def cartData(request):
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']
    return {'items':items, 'order': order, 'cartItems': cartItems}