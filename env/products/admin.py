from django.contrib import admin
from django.db import models
from .models import Products
# Register your models here.

class ProductManager(admin.ModelAdmin):
    list_display=('productName','model_category','stock','price','date_creation','is_available')
    prepopulated_fields={'slug':('productName',)}

admin.site.register(Products,ProductManager)