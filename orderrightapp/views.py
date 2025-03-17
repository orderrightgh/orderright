import random
import string
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import *
from .utils import cookieCart, cartData


def generate_random_number():
    # Generate a random number between 1 and 50 (inclusive)
    random_number = random.randint(1, 50)
    return random_number


goods = Products.objects.all()
random_number = generate_random_number()

# Create your views here.
def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    bestSellers = BestSellers.objects.all()
    context= {"products": goods,  'cartItems': cartItems, 'bestSellers': bestSellers,}
    return render(request, 'index.html', context)

def clothing(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = []
    packages = []
    
    type = Type.objects.all()
    for p in goods:
        # if p.type.string() == type[3]:
        if p.type.name == "clothing":

            products.append(p)
            print(p.type)
        else:
            packages.append(p)
    
    
    context= {"products": products, "packages":packages, 'cartItems': cartItems,}
    return render(request, 'clothing.html', context)


def laptops(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = []
    packages = []
    
    type = Type.objects.all()
    for p in goods:
        # if p.type.string() == type[3]:
        if p.type.name == "laptops":

            products.append(p)
            print(p.type)
        else:
            packages.append(p)
    
    
    context= {"products": products, "packages":packages, 'cartItems': cartItems,}
    return render(request, 'laptops.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    randomNum = generate_random_string(15)

    context = {'items':items, 'order': order, 'cartItems' : cartItems, 'randomNum': randomNum}
    return render(request, "checkout.html", context)


def accessories(request):
    return render(request, 'accessories.html')


def room(request):
    return render(request, 'room.html')


def phones(request):
    return render(request, 'phones.html')



def shop(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items':items, 'order': order, 'cartItems': cartItems, 'products': goods,}
    return render(request, 'shop.html', context)

def about(request):
    return render(request, 'about.html')



def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    

    context = {'items':items, 'order': order, 'cartItems': cartItems}
    return render(request, "cart.html", context)

def main(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    

    context = {'items':items, 'order': order, 'cartItems': cartItems}
    return render(request, "main.html", context)



def product_details(request, product_id):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = []
    packages = []
    type = Type.objects.all()
    for p in goods:
        if p.type == type[0]:
            products.append(p)
            print(p.type)
        else:
            packages.append(p)


    product = get_object_or_404(Products, pk=product_id)
    if product.description:
        list = (product.description).split(";")
        context = {"product": product, "products": products, "list": list, 'items':items, 'order': order, 'cartItems': cartItems, "random_number": random_number,}
    else:
        context = {"product": product, "products": products, "random_number": random_number, 'order': order, 'cartItems': cartItems}
    return render(request, 'product_details.html', context)

def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def generate_random_string(length):
    # Define the pool of characters (letters and digits)
    characters = string.ascii_letters + string.digits
    # Use random.choices to select random characters from the pool
    random_string = ''.join(random.choices(characters, k=length))
    return random_string



