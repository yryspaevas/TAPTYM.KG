from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Category_place)
admin.site.register(SubCategory_place)
admin.site.register(Place)
admin.site.register(Category_fun)
admin.site.register(Fun)
admin.site.register(Category_hotel)
admin.site.register(Hotel)

