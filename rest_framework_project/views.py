from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class User(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Joy Huang',
            'age': 34,
        }
        return Response(data)
