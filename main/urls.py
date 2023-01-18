from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('category_place', CategoryPlaceViewSet)
router.register('subcategory_place', SubCategoryPlaceViewSet)
router.register('place', PlaceViewSet)
router.register('category_fun', CategoryFunViewSet)
router.register('fun', FunViewSet)
router.register('category_hotel',CategoryHotelViewSet )
router.register('hotel', HotelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', poisk),
]
