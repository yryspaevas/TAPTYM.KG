from django.shortcuts import render, get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import mixins, generics
from rest_framework.decorators import api_view

from rest_framework.response import Response
from .serializers import *
from .paginations import HotelCommentPagination,FunCommentPagination, PlaceCommentPagination
from .models import *
from .permissions import IsAuthorOrReadOnly
from .models import *
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

class PlaceCommentLikeView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = PlaceCommentLike.objects.all()
    serializer_class = PlaceCommentLikeSerializer
    print("query",queryset)
    def get(self, request, pk):
        user = request.user
        
        comment = get_object_or_404(PlaceComment, id=pk)
        

        if PlaceCommentLike.objects.filter(user_place_comment=user, place_comment=comment).exists():
            PlaceCommentLike.objects.filter(user_place_comment=user, place_comment=comment).delete()
            return Response ('Like has been deleted')
        else:
            PlaceCommentLike.objects.create(user_place_comment=user, place_comment=comment)
            return Response("Liked", 200)
   

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

class FunCommentLikeView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = FunCommentLike.objects.all()
    serializer_class = FunCommentLikeSerializer

    def get(self, request, pk):
        user = request.user
        comment = get_object_or_404(FunComment, id=pk)

        if FunCommentLike.objects.filter(user_fun_comment=user, fun_comment=comment).exists():
            FunCommentLike.objects.filter(user_fun_comment=user, fun_comment=comment).delete()
            return Response ('Like has been deleted')
        else:
            FunCommentLike.objects.create(user_fun_comment=user, fun_comment=comment)
            return Response("Liked", 200)


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
    



class HotelCommentLikeView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = HotelCommentLike.objects.all()
    serializer_class = HotelCommentLikeSerializer

    def get(self, request, pk):
        user = request.user
        comment = get_object_or_404(HotelComment, id=pk)

        if HotelCommentLike.objects.filter(user_comment=user, hotel_comment=comment).exists():
            HotelCommentLike.objects.filter(user_comment=user, hotel_comment=comment).delete()
            return Response ('Like has been deleted')
        else:
            HotelCommentLike.objects.create(user_comment=user, hotel_comment=comment)
            return Response("Liked", 200)


class FavoritePlaceViewSet(ModelViewSet):
    queryset = FavoritePlace.objects.all()
    serializer_class = FavoritePlaceSerializer
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        new_queryset = queryset.filter(user=self.request.user)
        return new_queryset

@api_view(['POST'])
def add_favorite_place(request, place_id):
    user = request.user
    place = get_object_or_404(Place, id=place_id)

    if FavoritePlace.objects.filter(user=user, favorite=place).exists():
        FavoritePlace.objects.filter(user=user, favorite=place).delete()
        return Response('Deleted from favorite')
    else:
        FavoritePlace.objects.create(user=user, favorite=place, favorite_place=True)
        return Response('Added to favorites')

class FavoriteFunViewSet(ModelViewSet):
    queryset = FavoriteFun.objects.all()
    serializer_class = FavoriteFunSerializer
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        new_queryset = queryset.filter(user=self.request.user)
        return new_queryset

@api_view(['POST'])
def add_favorite_fun(request, fun_id):
    user = request.user
    fun = get_object_or_404(Fun, id=fun_id)

    if FavoriteFun.objects.filter(user=user, favorite=fun).exists():
        FavoriteFun.objects.filter(user=user, favorite=fun).delete()
        return Response('Deleted from favorite')
    else:
        FavoriteFun.objects.create(user=user, favorite=fun, favorite_fun=True)
        return Response('Added to favorites')

class FavoriteHotelViewSet(ModelViewSet):
    queryset = FavoriteHotel.objects.all()
    serializer_class = FavoriteHotelSerializer
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        new_queryset = queryset.filter(user=self.request.user)
        return new_queryset

@api_view(['POST'])
def add_favorite_hotel(request, hotel_id):
    user = request.user
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if FavoriteHotel.objects.filter(user=user, favorite=hotel).exists():
        FavoriteHotel.objects.filter(user=user, favorite=hotel).delete()
        return Response('Deleted from favorite')
    else:
        FavoriteHotel.objects.create(user=user, favorite=hotel, favorite_hotel=True)
        return Response('Added to favorites')

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

