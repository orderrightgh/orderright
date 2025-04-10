import random
import string
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import *
from .utils import cookieCart, cartData
from django.core.paginator import Paginator
from django.db.models import Q


def generate_random_number():
    # Generate a random number between 1 and 50 (inclusive)
    random_number = random.randint(1, 50)
    return random_number


# goods = Products.objects.all().order_by('?')
goods = Products.objects.select_related('type').prefetch_related('image')
random_number = generate_random_number()

# Create your views here.
# views.py


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.decorators.cache import cache_page
# cache_15min = cache_page(60 * 15)

def shop(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    # Set up pagination
    paginator = Paginator(goods, 12)  # Show 12 products per page
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        products = paginator.page(paginator.num_pages)
    
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'products': products,  # This is the paginated Page object
        'page_obj': products,  # Explicitly pass as page_obj for template clarity
    }
    return render(request, 'shop.html', context)


def search(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    # goods = Products.objects.all().order_by('?')
    

    # if request.method == "POST":
    #     searched = request.POST['searched']
        
    # searched_items = goods.filter(name__contains=searched)


    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()
        
        # Split search terms by spaces
        search_terms = searched.split()
        
        # Start with an empty Q object
        query = Q()
        
        for term in search_terms:
            # For each term, create OR condition between name and description
            query &= (Q(name__icontains=term) | Q(description__icontains=term))
        
        searched_items = Products.objects.filter(query).distinct()
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
    wears = []
    packages = []
    
    for p in goods:
        if p.type.name == "wears":

            wears.append(p)
            print(p.type)
        else:
            packages.append(p)

    paginator = Paginator(wears, 12)  # Show 12 products per page
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        products = paginator.page(paginator.num_pages)
    
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        "packages":packages,
        'products': products,  # This is the paginated Page object
        'page_obj': products,  # Explicitly pass as page_obj for template clarity
    }
    return render(request, 'wears.html', context)


def laptops(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    laptops =[]
    packages = []
    
    for p in goods:
        if p.type.name == "laptops":
            laptops.append(p)
            print(p.type)
        else:
            packages.append(p)
    
    paginator = Paginator(laptops, 12)  # Show 12 products per page
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        products = paginator.page(paginator.num_pages)
    
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        "packages":packages,
        'products': products,  # This is the paginated Page object
        'page_obj': products,  # Explicitly pass as page_obj for template clarity
    }
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
    order = data['order']
    items = data['items']
    accessories = []
    packages = []
    
    for p in goods:
        if p.type.name == "phone accessories":

            accessories.append(p)
            print(p.type)
        else:
            packages.append(p)
    
    paginator = Paginator(accessories, 12)  # Show 12 products per page
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        products = paginator.page(paginator.num_pages)

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        "packages":packages,
        'products': products,  # This is the paginated Page object
        'page_obj': products,  # Explicitly pass as page_obj for template clarity
    }
    return render(request, 'accessories.html', context)



def room(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    room = []
    packages = []
    
    for p in goods:
        if p.type.name == "room accessories":

            room.append(p)
            print(p.type)
        else:
            packages.append(p)
    
    paginator = Paginator(room, 12)  # Show 12 products per page
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        products = paginator.page(paginator.num_pages)

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        "packages":packages,
        'products': products,  # This is the paginated Page object
        'page_obj': products,  # Explicitly pass as page_obj for template clarity
    }
    return render(request, 'room.html', context)

def phones(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    phones = []
    packages = []
    
    for p in goods:
        if p.type.name == "phones":

            phones.append(p)
            print(p.type)
        else:
            packages.append(p)
    
    paginator = Paginator(phones, 12)  # Show 12 products per page
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        products = paginator.page(paginator.num_pages)

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        "packages":packages,
        'products': products,  # This is the paginated Page object
        'page_obj': products,  # Explicitly pass as page_obj for template clarity
    }
    return render(request, 'phones.html', context)




def faq(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items':items, 'order': order, 'cartItems': cartItems}
    return render(request, 'faq.html', context)


def contact(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items':items, 'order': order, 'cartItems': cartItems}
    return render(request, 'contact.html', context)

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