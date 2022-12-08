from django.shortcuts import render, redirect
from django.views import *
from asosiyapp.models import *
from userapp.models import *
from django.shortcuts import render
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import *

class MijozlarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        mijozlar = Mijoz.objects.all()
        serializers = MijozSerializer(mijozlar, many=True)
        return Response(serializers.data)

    def post(self, request):
        mijoz = request.data
        serializer = MijozSerializer(data=mijoz)
        if serializer.is_valid():
            serializer.save()
            natija = {"Succes": "True",
                      "Yangi mijoz": serializer.data}
            return Response(natija)
        return Response({"Ma'lumotda xatolik bor"})

class MahsulotlarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        mahsulotlar = Mahsulot.objects.all()
        serializers = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializers.data)

    def post(self, request):
        mahsulot = request.data
        serializer = MahsulotSerializer(data=mahsulot)
        if serializer.is_valid():
            serializer.save()
            natija = {"Succes": "True",
                      "Yangi mahsulot": serializer.data}
            return Response(natija)
        return Response({"Ma'lumotda xatolik bor"})

class MahsulotAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        mahsulot=Mahsulot.objects.get(id=pk)
        s = MahsulotSerializer(mahsulot)
        return Response(s.data)

    def put(self, request, pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        serializer = MahsulotSerializer(mahsulot, data=request.data)
        # sotuvchi = Mahsulot.objects.get(id=pk) #.sotuvchi.user
        if serializer.is_valid() and mahsulot.sotuvchi.user ==request.user:
            serializer.save()
            natija = {"Succes":"True",
                      "Changed data":serializer.data}
            return Response(natija)
        return Response({"xatolik":serializer.errors})

    def delete(self, request, pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        if mahsulot.sotuvchi.user == request.user:
            mahsulot.delete()
            return Response({"deleted"})
        return Response({"error":"xato"})

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            natija = {"Succes":"True",
                      "Yangi user":serializer.data}
            return Response(natija)
        return Response({"Xatolik":serializer.errors})