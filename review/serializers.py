from rest_framework import serializers
from account.models import User
from .models import *


class PlaceCommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.email')

    class Meta:
        model = PlaceComment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        reply = PlaceComment.objects.create(user_id=request.user, **validated_data)
        return reply


class FunCommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.email')

    class Meta:
        model = FunComment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        reply = FunComment.objects.create(user_id=request.user, **validated_data)
        return reply


class HotelCommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.email')

    class Meta:
        model = HotelComment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        reply = HotelComment.objects.create(user_id=request.user, **validated_data)
        return reply


class FavoritePlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoritePlace
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['user'] = instance.user.email
    #     representation['place'] = instance.place.title
    #     return representation

class FavoriteFunSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteFun
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['user'] = instance.user.email
    #     representation['fun'] = instance.fun.title
    #     return representation

class FavoriteHotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteHotel
        fields = '__all__'


class PlaceRatingSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.email')

    class Meta:
        model = PlaceRating
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        place_id = validated_data.get('place_id')
        place_rating = PlaceRating.objects.get_or_create(user_id=request.user, place_id=place_id)[0]
        place_rating.place_rating = validated_data['place_rating']
        place_rating.save()
        return place_rating

class FunRatingSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.email')

    class Meta:
        model = FunRating
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        fun_id = validated_data.get('fun_id')
        fun_rating = FunRating.objects.get_or_create(user_id=request.user, fun_id=fun_id)[0]
        fun_rating.fun_rating = validated_data['fun_rating']
        fun_rating.save()
        return fun_rating

class HotelRatingSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.email')

    class Meta:
        model = HotelRating
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        print(validated_data)
        hotel_id = validated_data.get('hotel_id')
        hotel_rating = HotelRating.objects.get_or_create(user_id=request.user, hotel_id=hotel_id)[0]
        hotel_rating.hotel_rating = validated_data['hotel_rating']
        hotel_rating.save()
        return hotel_rating
