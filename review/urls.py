from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('place_comment', PlaceCommentViewSet)
router.register('fun_comment', FunCommentViewSet)
router.register('hotel_comment', HotelCommentViewSet)
router.register('favorite_place', FavoritePlaceViewSet)
router.register('favorite_fun', FavoriteFunViewSet)
router.register('favorite_hotel', FavoriteHotelViewSet)
router.register('place_rating', PlaceRatingViewSet)
router.register('fun_rating', FunRatingViewSet)
router.register('hotel_rating', HotelRatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]