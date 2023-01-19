from django.shortcuts import render
from django.db.models import Avg
from django.db.models import Count

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser
# from .paginations import HotelPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.pagination import PageNumberPagination


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

    @swagger_auto_schema(manual_parameters=[
            openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() # Product.objects.all()
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(info__icontains=q))

        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)

    @action(['GET'], detail=False)
    def filter_place(self, request):
        cat_id = request.query_params.get('category_id')
        subcat_id = request.query_params.get('sub_category_id')
        queryset = self.get_queryset()
        if cat_id  and subcat_id is not None:
            queryset = queryset.filter(category_id=cat_id, sub_category_id=subcat_id)
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)

    

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
    
    @swagger_auto_schema(manual_parameters=[
            openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() # Product.objects.all()
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(info__icontains=q))

        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)
        
    @action(['GET'], detail=False)
    def top_three(self, request):
        queryset = self.get_queryset()[:3]
        return Response(self.get_serializer(queryset, many=True).data)

    @action(['GET'], detail=False)
    def filter_fun(self, request):
        cat_id = request.query_params.get('category_id')
        queryset = self.get_queryset()
        if cat_id is not None:
            queryset = queryset.filter(category_id=cat_id)
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
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

    @swagger_auto_schema(manual_parameters=[
            openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() # Product.objects.all()
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(info__icontains=q))

        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)
    @action(['GET'], detail=False)
    def filter_hotel(self, request):
        cat_id = request.query_params.get('category_id')
        queryset = self.get_queryset()
        if cat_id is not None:
            queryset = queryset.filter(category_id=cat_id)
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def poisk(request):
    q = request.query_params.get('q')
    queryset1 = Fun.objects.filter(Q(name__icontains=q) | Q(info__icontains=q))
    queryset2 = Place.objects.filter(Q(name__icontains=q) | Q(info__icontains=q))
    queryset3 = Hotel.objects.filter(Q(name__icontains=q) | Q(info__icontains=q))
    res = []
    res.extend(FunSerializer(queryset1, many=True).data)
    res.extend(PlaceSerializer(queryset2, many=True).data)
    res.extend(HotelSerializer(queryset3, many=True).data)

    paginator = PageNumberPagination()
    pagination = paginator.paginate_queryset(res, request)
    if pagination:
        return paginator.get_paginated_response(pagination)
    return Response(res)


