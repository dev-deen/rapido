from django.shortcuts import render
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class CreateListReviewAPIView(APIView):
    def get(self, request, format=None):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get('is_user_to_driver_review', True):
                driver = request.data.get('driver')
                serializer.save(user=request.user, driver_id=driver)
            else:
                user = request.data.get('user')
                serializer.save(driver=request.user, user_id=user)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


