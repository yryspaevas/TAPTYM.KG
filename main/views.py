from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action




class CategoryPlaceViewSet(ModelViewSet):
    queryset = Category_place.objects.all()
    serializer_class = CategoryPlaceSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class SubCategoryPlaceViewSet(ModelViewSet):
    queryset = SubCategory_place.objects.all()
    serializer_class = SubCategoryPlaceSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class CategoryFunViewSet(ModelViewSet):
    queryset = Category_fun.objects.all()
    serializer_class = CategoryFunSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class FunViewSet(ModelViewSet):
    queryset = Fun.objects.all()
    serializer_class = FunSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class CategoryHotelViewSet(ModelViewSet):
    queryset = Category_hotel.objects.all()
    serializer_class = CategoryHotelSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]   

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() # Product.objects.all()
        if q:
            queryset = queryset.filter(Q(title__icontains=q))

        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)