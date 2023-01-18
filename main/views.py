from django.shortcuts import render
from django.db.models import Avg
from django.db.models import Count

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
# from .paginations import HotelPagination


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
    @action(['GET'], detail=False)
    def top_three(self, request):
        queryset = self.get_queryset()[:3]
        return Response(self.get_serializer(queryset, many=True).data)

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

    @action(['GET'], detail=False)
    def top_three(self, request):
        queryset = self.get_queryset()[:3]
        return Response(self.get_serializer(queryset, many=True).data)

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
    # pagination_class = HotelPagination
    
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]  

    @action(['GET'], detail=False)
    def top_three(self, request):
        queryset = self.get_queryset()[:3]
        return Response(self.get_serializer(queryset, many=True).data)
    # def get_top_3_hotels_with_most_comments():
    #     top_3_hotels = Hotel.objects.annotate(num_comments=Count('hotel_comments')).order_by('-num_comments')[:3]
    #     return top_3_hotels 
    # def top_hotels_view(request):
    #     queryset = HotelViewSet.queryset.all()[:3]
    #     serializer = HotelSerializer(queryset, many=True)
    #     return Response(serializer.data)