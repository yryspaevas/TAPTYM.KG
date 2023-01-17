from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(PlaceComment)
admin.site.register(FavoritePlace)
admin.site.register(PlaceRating)
admin.site.register(FunComment)
admin.site.register(FavoriteFun)
admin.site.register(FunRating)
admin.site.register(HotelComment)
admin.site.register(FavoriteHotel)
admin.site.register(HotelRating)