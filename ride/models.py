from django.db import models
from user.models import User
# Create your models here.
class Ride(models.Model):
    RIDE_CHOICES = (
        ('R', 'Requested'),
        ('A', 'Approved'),
        ('C', 'Completed'),
        ('W', 'Withdrawn')
    )
    ride_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ride')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_ride')
    ride_status = models.CharField(max_length=1, choices=RIDE_CHOICES)
    pickup_location = models.TextField()
    drop_location = models.TextField()
    fare = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return f'R{self.ride_id} {self.get_ride_status_display()}'

class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=60, unique=True, blank=False, null=False)
    base_fare = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)


class Vehicle(models.Model):
    vehicle_no = models.CharField(max_length=10, blank=False, null=False)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, related_name='vehicle')
    vehicle_name = models.CharField(max_length=122, blank=True, null=True)
    colour = models.CharField(max_length=15, blank=True, null=True)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicle')

class DriverIncome(models.Model):
    INCOME_CHOICES = (
        ('INCENTIVE', 'incentive'),
        ('RIDE_FEE', 'ride_fee')
    )
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_income')
    income_type = models.CharField(max_length=10, choices=INCOME_CHOICES, blank=False, null=False)
    income = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_reviews')
    is_user_to_driver_review = models.BooleanField(default=True)
    rating = models.IntegerField(blank = False, null=False)

class RideCancellation(models.Model):
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE, related_name='ride_cancellation')
    comment = models.CharField(max_length=255, blank=False, null=False)
