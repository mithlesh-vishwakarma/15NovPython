from django.contrib import admin
from product_management.models import *

# Register your models here.


# class ProductDisplay(admin.ModelAdmin):
#     list_display = ["id", "name", "price", "qty", "image"]


admin.site.register(Product)
