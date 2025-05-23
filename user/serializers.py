from rest_framework import serializers
from .models import User
from django.db.models import Avg
from ride.models import Review

class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)
    user_rating = serializers.SerializerMethodField()
    driver_rating = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['user_id', 'phone', 'email', 'password', 'gender', 'user_rating', 'driver_rating', 'is_driver', 'is_staff']

    def create(self, validated_data):
        email = validated_data.get('email')
        phone = validated_data.get('phone')
        validated_data['username'] = email or phone
        user = User.objects.create_user(**validated_data)
        return user

    def get_user_rating(self, obj):
        reviews = Review.objects.filter(user=obj, is_user_to_driver_review=False)
        avg = reviews.aggregate(
            Avg('rating')
        )['rating__avg']
        return round(avg, 2) if avg is not None else 0.0
    
    def get_driver_rating(self, obj):
        reviews = Review.objects.filter(user=obj, is_user_to_driver_review=True)
        avg = reviews.aggregate(
            Avg('rating')
        )['rating__avg']
        return round(avg, 2) if avg is not None else 0.0


