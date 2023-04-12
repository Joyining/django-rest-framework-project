from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from my_app.serializers import ProductSerializer
from my_app.models import Product


class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        query_set = Product.objects.all()
        serializer = ProductSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
