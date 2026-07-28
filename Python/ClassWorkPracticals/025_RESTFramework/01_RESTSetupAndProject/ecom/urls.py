from django.urls import path
from ecom.views import *

urlpatterns = [
    path("categories",CategoryAPI.as_view()),
    # path("categories",CategoryAPIByID.as_view()),

    # path("products",ProductAPI.as_view()),
    # path("products",ProdcutAPIById.as_view())
]
