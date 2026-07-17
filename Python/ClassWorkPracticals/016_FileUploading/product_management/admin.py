from django.contrib import admin
from product_management.models import Product,Category

# Register your models here.


# class ProductDisplay(admin.ModelAdmin):
#     list_display = ["id", "name", "price", "qty", "image"]

admin.site.register(Category)
admin.site.register(Product)
