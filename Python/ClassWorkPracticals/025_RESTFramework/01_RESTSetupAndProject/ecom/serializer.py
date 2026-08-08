from rest_framework import serializers
from ecom.models import *

class CategorySerialaizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


# class ProductSerializer(serializers,ModelSerializer):
#     class Meta:
#         model=Product,
#         fields="__all__"