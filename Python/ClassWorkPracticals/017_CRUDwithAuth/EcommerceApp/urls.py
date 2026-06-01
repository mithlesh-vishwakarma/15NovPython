from django.urls import path
from EcommerceApp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("registration",registration,name="registration"),
    path("logout",logout_user,name="logout"),
    path("product_form", product_form, name="product_form"),
    path("product_list", product_list, name="product_list"),
    path("edit_product/<int:pk>/", edit_product, name="edit_product"),
    path("delete_product/<int:pk>/", delete_product, name="delete_product"),
]
