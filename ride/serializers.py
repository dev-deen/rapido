from rest_framework import serializers
from . import models
from user.serializers import UserSerializer

class RideSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    driver = UserSerializer(read_only=True)
    ride_id = serializers.ReadOnlyField()
    class Meta:
        model = models.Ride
        fields = '__all__'
    
class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehicleType
        fields = ['vehicle_type', 'base_fair']
    
class VehicleSerializer(serializers.ModelSerializer):
    id = serializer.ReadOnlyField()
    vehicle_type = VehicleTypeSerializer(read_only=True)
    driver = UserSerializer(read_only=True)
    class Meta:
        model = models.Vehicle
        fields = '__all__'

class DriverIncomeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    driver = UserSerializer(read_only=True)
    class Meta:
        model = models.DriverIncome
        fields = '__all__'

class RideCancellationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.RideCancellation
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    id = serializer.ReadOnly()
    user = UserSerializer(read_only=True)
    driver = UserSerializer(read_only=True)
    class Meta:
        model = models.Rating
        fields = '__all__'

