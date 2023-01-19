from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .serializers import *
from .paginations import HotelCommentPagination,FunCommentPagination, PlaceCommentPagination
from .permissions import IsAuthorOrReadOnly
# from main.views import HotelViewSet
# from main.serializers import HotelSerializer

# Create your views here.


class PlaceCommentViewSet(ModelViewSet):
    queryset = PlaceComment.objects.all()
    serializer_class = PlaceCommentSerializer
    pagination_class = PlaceCommentPagination

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

   

class FunCommentViewSet(ModelViewSet):
    queryset = FunComment.objects.all()
    serializer_class = FunCommentSerializer
    pagination_class = FunCommentPagination

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]

class HotelCommentViewSet(ModelViewSet):
    queryset = HotelComment.objects.all()
    serializer_class = HotelCommentSerializer
    pagination_class = HotelCommentPagination

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        elif self.action == 'create':
            return [IsAuthenticatedOrReadOnly()]
        elif self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAdminUser()]
    


class FavoritePlaceViewSet(ModelViewSet):
    queryset = FavoritePlace.objects.all()
    serializer_class = FavoritePlaceSerializer
    permission_classes = [IsAuthorOrReadOnly]

class FavoriteFunViewSet(ModelViewSet):
    queryset = FavoriteFun.objects.all()
    serializer_class = FavoriteFunSerializer
    permission_classes = [IsAuthorOrReadOnly]

class FavoriteHotelViewSet(ModelViewSet):
    queryset = FavoriteHotel.objects.all()
    serializer_class = FavoriteHotelSerializer
    permission_classes = [IsAuthorOrReadOnly]

class PlaceRatingViewSet(ModelViewSet):
    queryset = PlaceRating.objects.all()
    serializer_class = PlaceRatingSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAuthorOrReadOnly()]

class FunRatingViewSet(ModelViewSet):
    queryset = FunRating.objects.all()
    serializer_class = FunRatingSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAuthorOrReadOnly()]

class HotelRatingViewSet(ModelViewSet):
    queryset = HotelRating.objects.all()
    serializer_class = HotelRatingSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запросы на листинг и детализацию
            return [] # то разрешаем всем
        return [IsAuthorOrReadOnly]

