from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Products)
admin.site.register(Type)
admin.site.register(BestSellers)
admin.site.register(NewArrivals)
admin.site.register(Post)



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of empty forms to display by default
    can_delete = True

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Products, ProductAdmin)