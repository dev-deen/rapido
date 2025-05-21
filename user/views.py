from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response 
# Create your views here.
class CreateListUser(APIView):
    
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)