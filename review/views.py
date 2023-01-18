from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import *

# Create your views here.


class PlaceCommentViewSet(ModelViewSet):
    queryset = PlaceComment.objects.all()
    serializer_class = PlaceCommentSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class FunCommentViewSet(ModelViewSet):
    queryset = FunComment.objects.all()
    serializer_class = FunCommentSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class HotelCommentViewSet(ModelViewSet):
    queryset = HotelComment.objects.all()
    serializer_class = HotelCommentSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class FavoritePlaceViewSet(ModelViewSet):
    queryset = FavoritePlace.objects.all()
    serializer_class = FavoritePlaceSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class FavoriteFunViewSet(ModelViewSet):
    queryset = FavoriteFun.objects.all()
    serializer_class = FavoriteFunSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class FavoriteHotelViewSet(ModelViewSet):
    queryset = FavoriteHotel.objects.all()
    serializer_class = FavoriteHotelSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class PlaceRatingViewSet(ModelViewSet):
    queryset = PlaceRating.objects.all()
    serializer_class = PlaceRatingSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class FunRatingViewSet(ModelViewSet):
    queryset = FunRating.objects.all()
    serializer_class = FunRatingSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class HotelRatingViewSet(ModelViewSet):
    queryset = HotelRating.objects.all()
    serializer_class = HotelRatingSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

