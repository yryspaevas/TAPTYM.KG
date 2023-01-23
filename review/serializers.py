from django.db.models import Count
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

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # rep["place_likes"] = PlaceCommentLikeSerializer(instance.place_likes.all(), many=True).data
        rep["place_likes"] = instance.place_likes.all().count()
        return rep

class PlaceCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceCommentLike
        fields = '__all__'


class FunCommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.email')

    class Meta:
        model = FunComment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        reply = FunComment.objects.create(user_id=request.user, **validated_data)
        return reply

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # rep["fun_likes"] = FunCommentLikeSerializer(instance.fun_likes.all(), many=True).data
        rep["fun_likes"] = instance.fun_likes.all().count()
        return rep

class FunCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunCommentLike
        fields = '__all__'


class HotelCommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.email')
    # hotel_comment_likes_count = serializers.SerializerMethodField()
    # hotel_comment_dislikes_count = serializers.SerializerMethodField()

    class Meta:
        model = HotelComment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        reply = HotelComment.objects.create(user_id=request.user, **validated_data)
        return reply

    # def create_hotel_comment(self, validated data):


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # rep["hotel_li"] = HotelCommentLikeSerializer(instance.hotel_likes.all(), many=True).data
        rep["hotel_likes"] = instance.hotel_likes.all().count()
        return rep
    

class HotelCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelCommentLike
        fields = '__all__'
    

# class HotelCommentDislikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HotelCommentDislike
#         fields = '__all__'


class FavoritePlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoritePlace
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs

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

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs

class FavoriteHotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteHotel
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs


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
