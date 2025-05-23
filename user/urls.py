from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.CreateListUserAPIView.as_view(), name='create-list-users'),
    path('<int:pk>', views.RetreiveUpdateDestroyUserAPIView.as_view(), name='retreive-user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)