from codecs import register
from django.contrib import admin
from foodiespot.models import Restaurant
# Register your models here.

class displayRestaurant(admin.ModelAdmin):
  list_display=["id","name","cuisine","rating"]
  search_fields=["name","cuisine"]
  list_filter=["cuisine"]



admin.site.register(Restaurant,displayRestaurant)
