from itertools import product
from re import I
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .products import products
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def get_routes(request):
    return Response('hello')


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serailizer = ProductSerializer(products, many=True)
    return Response(serailizer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)