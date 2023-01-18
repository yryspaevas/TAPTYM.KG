from rest_framework.serializers import ModelSerializer
from .models import Category_fun, Category_hotel, Category_place, SubCategory_place, Place, Fun, Hotel
from review.serializers import HotelCommentSerializer, FunCommentSerializer, PlaceCommentSerializer


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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['place_comments'] = PlaceCommentSerializer(instance.fun_comments.all(), many=True).data
        representation['place_rating'] = instance.get_average_rating()
        return representation

class CategoryFunSerializer(ModelSerializer):
    class Meta:
        model = Category_fun
        fields= '__all__'

class FunSerializer(ModelSerializer):
    class Meta:
        model = Fun
        fields= '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['fun_comments'] = FunCommentSerializer(instance.fun_comments.all(), many=True).data
        representation['fun_rating'] = instance.get_average_rating()
        return representation

class CategoryHotelSerializer(ModelSerializer):
    class Meta:
        model = Category_hotel
        fields= '__all__'

class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields= '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['hotel_comments'] = HotelCommentSerializer(instance.hotel_comments.all(), many=True).data
        representation['hotel_rating'] = instance.get_average_rating()
        

        # representation['user'] = instance.user.email
        # representation['fun'] = instance.fun.title
        return representation
        
        
        # rep['rating'] = instance.average_rating
        # rep['likes'] = instance.movie_likes.all().count()
        # rep['favorites'] = instance.movie_favourite.filter(favorite=True).count()
        # return rep
    