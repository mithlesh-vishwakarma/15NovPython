from django.contrib import admin
from foodiespot.models import *
# Register your models here.

class displayRestaurant(admin.ModelAdmin):
  list_display=["name","location","rating"]

class displayCuisin(admin.ModelAdmin):
  list_display=["name","description","restaurant"]



admin.site.register(Restaurant,displayRestaurant)
admin.site.register(Cuisin,displayCuisin)
