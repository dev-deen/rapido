from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response 
from django.http import Http404

# Create your views here.
class CreateListUserAPIView(APIView):
    
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


class RetreiveUpdateDestroyUserAPIView(APIView):

    def get_object(self, id):
        return get_object_or_404(User, pk=id)   

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=204)