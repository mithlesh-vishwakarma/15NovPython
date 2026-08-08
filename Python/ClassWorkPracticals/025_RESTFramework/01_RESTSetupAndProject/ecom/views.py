from django.shortcuts import render
from ecom.models import *
from rest_framework.response import Response
from rest_framework.decorators import APIView
from ecom.serializer import *

# Create your views here.

class CategoryAPI(APIView):
    def get(self,request):
        categories=Category.objects.all()
        ser=CategorySerialaizer(categories,many=true)
        return Response({"data":ser.data})

    def post(self,request):
        ser=CategorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data})
        else: 
            return Response({"errors":ser.errors})
        return Response("post is calling")

# class CategoryAPIById(APIView):
#     def get(self,request,id):
#         categories=Category.objects.all()
#         ser=CategorySerializer(categories,)



#     def post(self,request,id):
#         pass

