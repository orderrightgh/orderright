from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('phones', views.phones, name = 'phones'),
    path('accessories', views.accessories, name = 'accessories'),
    path('room', views.room, name = 'room'),
    path('laptops', views.laptops, name = 'laptops'),
    path('wears', views.wears, name = 'wears'),
    path('search', views.search, name = 'search'),
    path('shop', views.shop, name = 'shop'),
    path('cart', views.cart, name = 'cart'),
    path('checkout', views.checkout, name = 'checkout'),
    path('update_item', views.update_item, name ="update_item"),
    path('processOrder', views.processOrder, name ="processOrder"),
    path('faq', views.faq, name = 'faq'),
    path('contact', views.contact, name = 'contact'),
    path('blog', views.blog, name = 'blog'),
    path('product_details/<int:product_id>', views.product_details, name = 'product_details'),
]
