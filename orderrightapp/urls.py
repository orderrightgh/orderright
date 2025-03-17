from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('phones', views.phones, name = 'phones'),
    path('accessories', views.accessories, name = 'accessories'),
    path('room', views.room, name = 'room'),
    path('laptops', views.laptops, name = 'laptops'),
    path('clothing', views.clothing, name = 'clothing'),
    path('shop', views.shop, name = 'shop'),
    path('cart', views.cart, name = 'cart'),
    path('checkout', views.checkout, name = 'checkout'),
    path('update_item', views.update_item, name ="update_item"),
    path('about', views.index, name = 'about'),
    path('product_details/<int:product_id>', views.product_details, name = 'product_details'),
]
