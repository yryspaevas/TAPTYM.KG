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
# router.register('likes/', LikeView.as_view())
# router.register('hotel_likes', HotelCommentLikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('hotel_likes/<int:pk>/', HotelCommentLikeView.as_view()),
    path('fun_likes/<int:pk>/', FunCommentLikeView.as_view()),
    path('place_likes/<int:pk>/', PlaceCommentLikeView.as_view()),

]