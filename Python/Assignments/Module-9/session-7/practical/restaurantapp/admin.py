from restaurantapp.models import Restuarant
from django.contrib import admin

# Register your models here.
class displayRestaurant(admin.ModelAdmin):
  list_display=["id","name","cuisine","rating"]


admin.site.register(Restuarant,displayRestaurant)