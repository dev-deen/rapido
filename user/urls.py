from django.urls import path
from . import views

urlpatterns = [
    path('', CreateListAPIView.as_view(), name='create-users'),
]
