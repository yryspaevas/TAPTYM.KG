from django.shortcuts import render
from django.db.models import Avg

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser


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
    queryset = Place.objects.all().annotate(rating=Avg('place_rating__place_rating')).order_by('-place_rating')
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
    queryset = Fun.objects.all().annotate(rating=Avg('fun_rating__fun_rating')).order_by('-fun_rating')
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
    queryset = Hotel.objects.all().annotate(rating=Avg('hotel_rating__hotel_rating')).order_by('-hotel_rating')
    serializer_class = HotelSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]   