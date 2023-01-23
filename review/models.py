from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.db.models import Count

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from account.models import User
from main.models import Place, Fun, Hotel


class PlaceComment(models.Model):
    user_id = models.ForeignKey(User, related_name='place_comments',on_delete=models.CASCADE)
    place_id = models.ForeignKey(Place,related_name='place_comments',on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PlaceCommentLike(models.Model):
    user_place_comment = models.ForeignKey(User, related_name='place_likes', on_delete=models.CASCADE)
    place_comment = models.ForeignKey(PlaceComment, related_name='place_likes', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='like_place', blank=True)

    def likes_quantity(self):
        return self.likes.count()


class FavoritePlace(models.Model):
    user_id = models.ForeignKey(User, related_name='place_favorite', on_delete= models.CASCADE)
    place_id = models.ForeignKey(Place, related_name='favorite', on_delete=models.CASCADE)
    favorite_place = models.BooleanField(default=False)

class PlaceRating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='place_rating')
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_rating')
    place_rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)], default=0)


class FunComment(models.Model):
    user_id = models.ForeignKey(User, related_name='fun_comments',on_delete=models.CASCADE)
    fun_id = models.ForeignKey(Fun,related_name='fun_comments',on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
class FunCommentLike(models.Model):
    user_fun_comment = models.ForeignKey(User, related_name='fun_likes', on_delete=models.CASCADE)
    fun_comment = models.ForeignKey(FunComment, related_name='fun_likes', on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name='like_fun')

    def likes_quantity(self):
        return self.likes.count()
    



class FavoriteFun(models.Model):
    user_id = models.ForeignKey(User, related_name='fun_favorite', on_delete= models.CASCADE)
    fun_id = models.ForeignKey(Fun, related_name='favorite', on_delete=models.CASCADE)
    favorite_fun = models.BooleanField(default=False)

class FunRating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fun_rating')
    fun_id = models.ForeignKey(Fun, on_delete=models.CASCADE, related_name='fun_rating')
    fun_rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)], default=0)

class HotelCommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='hotel_likes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class HotelComment(models.Model):
    user_id = models.ForeignKey(User, related_name='hotel_comments',on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotel,related_name='hotel_comments',on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

# class HotelCommentLike(models.Model):
#     user_comment = models.ForeignKey(User, related_name='hotel_comment_likes', on_delete=models.CASCADE)
#     hotel_comment = models.ForeignKey(HotelComment, related_name='hotel_comment_likes', on_delete=models.CASCADE)
   
#     # likes = models.ManyToManyField(User, related_name='like_hotel')

    # def likes_quantity(self):
    #     return self.objects.count()
   

class FavoriteHotel(models.Model):
    user_id = models.ForeignKey(User, related_name='hotel_favorite', on_delete= models.CASCADE)
    hotel_id = models.ForeignKey(Hotel, related_name='favorite', on_delete=models.CASCADE)
    favorite_hotel = models.BooleanField(default=False)

class HotelRating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hotel_rating')
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_rating')
    hotel_rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)], default=0)

    

