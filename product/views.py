from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from product.serializers import ProductSerializer
from rest_framework.response import Response

from product.models import Product


class ProductListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.order_by('-size')
        return {'products': products}


class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        product = Product.objects.get(pk=kwargs.get('pk'))
        return {'product': product}


class ProductListRest(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 1
        # Product.objects.create(
        #     title=serializer.validated_data['title'],
        #     description=serializer.validated_data['description'],
        #     price=serializer.validated_data['price'],
        #     size=serializer.validated_data['size'],
        #     color=serializer.validated_data['color'],
        #     image=serializer.validated_data['image']
        # )

        # 2
        # Product.objects.create(**serializer.validated_data)

        # 3
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
