from django.urls import path
from django.views import View
from django.contrib import admin
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('mijozlar/', MijozlarAPIView.as_view()),
    path('mahsulotlar/', MahsulotlarAPIView.as_view()),
    path('mahsulot/<int:pk>/', MahsulotAPIView.as_view()),
    path('users/', UserAPIView.as_view(), name='users'),
    path('get_token/', obtain_auth_token, name='api_token_auth'),
]