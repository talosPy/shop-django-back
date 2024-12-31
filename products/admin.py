from django.contrib import admin
from .models import Product
from django.contrib.auth.models import User  



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "image")
    search_fields = ("name",)


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_staff")  
    search_fields = ("username",)  


