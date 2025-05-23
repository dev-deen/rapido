from django.urls import path
from . import views

urlpatterns = [
    path('reviews', views.CreateListReviewAPIView.as_view(), name='create-list-review'),
]