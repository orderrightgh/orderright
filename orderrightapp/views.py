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


goods = Products.objects.all().order_by('?')    
random_number = generate_random_number()

# Create your views here.
def search(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    

    if request.method == "POST":
        searched = request.POST['searched']
        
    searched_items = goods.filter(name__contains=searched)

    context= {"products": goods,  'searched': searched, 'searched_items':searched_items, 'items':items, 'order': order, 'cartItems': cartItems}
    return render(request, 'search.html', context)


def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    bestSellers = BestSellers.objects.all().order_by('?') 
    posts = Post.objects.all().order_by('?') 
    newArrivals = NewArrivals.objects.all().order_by('?') 
    context= {"products": goods, 'items':items, 'order': order, 'cartItems': cartItems, 'bestSellers': bestSellers, 'newArrivals': newArrivals, 'posts': posts,}
    return render(request, 'index.html', context)

def wears(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = []
    packages = []
    
    for p in goods:
        if p.type.name == "wears":

            products.append(p)
            print(p.type)
        else:
            packages.append(p)
    context= {"products": products, "packages":packages, 'items':items, 'order': order, 'cartItems': cartItems,}
    return render(request, 'wears.html', context)


def laptops(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products =[]
    packages = []
    
    for p in goods:
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
    data = cartData(request)
    cartItems = data['cartItems']
    products = []
    packages = []
    
    for p in goods.order_by('?'):
        if p.type.name == "phone accessories":

            products.append(p)
            print(p.type)
        else:
            packages.append(p)
    
    
    context= {"products": products, "packages":packages, 'cartItems': cartItems,}
    return render(request, 'accessories.html', context)


def room(request):
    return render(request, 'room.html')


def phones(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = []
    packages = []
    
    for p in goods.order_by('?'):
        if p.type.name == "phones":

            products.append(p)
            print(p.type)
        else:
            packages.append(p)
    
    
    context= {"products": products, "packages":packages, 'cartItems': cartItems,}
    return render(request, 'phones.html', context)



def shop(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items':items, 'order': order, 'cartItems': cartItems, 'products': goods,}
    return render(request, 'shop.html', context)

def faq(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items':items, 'order': order, 'cartItems': cartItems}
    return render(request, 'faq.html', context)

def contact(request):
    return render(request, 'contact.html')

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
    product = get_object_or_404(Products, pk=product_id)
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    product_type = product.type.name



    relatedProducts = []
    packages = []
    for p in goods:
        if (p.type.name == product_type) & (p.id != product_id): 
            relatedProducts.append(p)
            print(p.type)
        else:
            packages.append(p)

    
    if product.description:
        list = (product.description).split(";")
        context = {"product": product, "relatedProducts": relatedProducts, "list": list, 'items':items, 'order': order, 'cartItems': cartItems, "random_number": random_number,}
    else:
        context = {"product": product, "relatedProducts": relatedProducts, "random_number": random_number, 'order': order, 'cartItems': cartItems, 'items':items}
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
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string



def blog(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    postsh = Post.objects.all().order_by('?') 
    context= {"products": goods, 'items':items, 'order': order, 'cartItems': cartItems, 'posts': postsh,}
    return render(request, 'blog.html', context)





def processOrder(request):
    data = json.loads(request.body)
    

    return JsonResponse("Payment complete", safe=False)