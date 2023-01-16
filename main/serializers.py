from rest_framework.serializers import ModelSerializer
from .models import Category_fun, Category_hotel, Category_place, SubCategory_place, Place, Fun, Hotel

class CategoryPlaceSerializer(ModelSerializer):
    class Meta:
        model = Category_place
        fields = '__all__'

class SubCategoryPlaceSerializer(ModelSerializer):
    class Meta:
        model = SubCategory_place
        fields= '__all__'

class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields= '__all__'

class CategoryFunSerializer(ModelSerializer):
    class Meta:
        model = Category_fun
        fields= '__all__'

class FunSerializer(ModelSerializer):
    class Meta:
        model = Fun
        fields= '__all__'

class CategoryHotelSerializer(ModelSerializer):
    class Meta:
        model = Category_hotel
        fields= '__all__'

class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields= '__all__'