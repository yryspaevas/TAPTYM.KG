from django.shortcuts import render, get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import mixins, generics
from rest_framework.decorators import api_view

from rest_framework.response import Response
from .serializers import *
from .paginations import HotelCommentPagination,FunCommentPagination, PlaceCommentPagination
from .models import *
from .permissions import IsAuthorOrReadOnly
# from main.views import HotelViewSet
# from main.serializers import HotelSerializer

# Create your views here.


class PlaceCommentViewSet(ModelViewSet):
    queryset = PlaceComment.objects.all()
    serializer_class = PlaceCommentSerializer
    pagination_class = PlaceCommentPagination
    
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

