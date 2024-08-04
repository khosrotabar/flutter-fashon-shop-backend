from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
from django.db.models import Count
import random

# Create your views here.
class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    queryset = models.Category.objects.all()

class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        queryset = models.Category.objects.all()
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:5]
    
class BrandCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    queryset = models.Brand.objects.all()
    
class ProductCategoryList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = models.Product.objects.all()
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:20]

class PopularProductsList(generics.ListAPIView):
    serializer_class =serializers.ProductSerializer
    
    def get_queryset(self):
        queryset = models.Product.objects.filter(rating__gte=4.0, rating__lte=5.0)
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:20]

class ProductsListByClothesType(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self, request):
        query = request.query_params.get('clothes_type', None)

        if query:
            queryset = models.Product.objects.filter(clothes_type=query)
            queryset = queryset.annotate(random_order=Count('id'))

            products_list = list(queryset)
            random.shuffle(products_list)

            limited_products = products_list[:20]

            serializer = serializers.ProductSerializer(limited_products, many=True)
    
            return Response(serializer.data)
        else:
            return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)

class SilmilarProducts(APIView):

    def get(self, request):
        query = request.querY_params.get('category', None)

        if query:
            products = models.Product.objects.filter(category = query)

            product_list = list(products)
            
            random.shuffle(product_list)

            limited_products = product_list[:6]

            serializer = serializers.ProductSerializer(limited_products, many=True)

            return Response(serializer.data)
        else:
            return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)

class SearchProductsByTitle(APIView):

    def get(self, request):
        query = request.query_params.get('q', None)

        if query:
            products = models.Product.objects.filter(title_icontains=query)

            serializer = serializers.ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)

class FilterProductsByCategory(APIView):
    def get(self, request):
        query = request.query_params.get('category', None)

        if query:
            products = models.Product.objects.filter(category = query)

            serializer = serializers.ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)