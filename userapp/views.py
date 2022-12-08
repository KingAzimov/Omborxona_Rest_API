from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import *
from rest_framework.authtoken.admin import User
from rest_framework.views import APIView


# class UsersView(APIView):
#     def get(self, request):
#         users = User.objects.all()

