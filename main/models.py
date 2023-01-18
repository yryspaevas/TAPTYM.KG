from django.db import models


# Create your models here.


class Category_place(models.Model):
    title = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории заведений"

class SubCategory_place(models.Model):
    category = models.ManyToManyField(Category_place, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кухня"
        verbose_name_plural = "Кухня"


class Place(models.Model):
    group = models.CharField(max_length=255, choices=[('food', 'ЕДА'), ('fun', 'РАЗВЛЕЧЕНИЯ'), ('hotel', 'РАЗМЕЩЕНИЕ')])
    category = models.ManyToManyField(Category_place, related_name="category_place")
    sub_category = models.ManyToManyField(SubCategory_place, related_name="subcategory_place")
    name = models.CharField(max_length=255)
    info = models.TextField()
    address = models.CharField(max_length=255)
    hours = models.TextField(blank=True)
    image = models.ImageField(upload_to='place', blank=True)
    map_link = models.CharField(max_length=255, blank=True)
    place_link = models.CharField(max_length=255, blank=True)
    avg_price= models.CharField(max_length=255, blank=True)


    class Meta:
        verbose_name = "Еда"
        verbose_name_plural = "Еда"

    def get_average_rating(self):
        ratings = self.place_rating.all()
        values = [i.place_rating for i in ratings]
        if ratings.exists():
            return sum(values) // ratings.count()
        return 0

class Category_fun(models.Model):
    
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории развлечений"

class Fun(models.Model):
    group = models.CharField(max_length=255, choices=[('food', 'ЕДА'), ('fun', 'РАЗВЛЕЧЕНИЯ'), ('hotel', 'РАЗМЕЩЕНИЕ')])
    category = models.ForeignKey(Category_fun, related_name="category_fun", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    info = models.TextField()
    address = models.CharField(max_length=255)
    hours = models.TextField(blank=True)
    image = models.ImageField(upload_to='fun', blank=True)
    map_link = models.CharField(max_length=255, blank=True) 
    fun_link = models.CharField(max_length=255, blank=True)


    class Meta:
        verbose_name = "Развлечение"
        verbose_name_plural = "Развлечения"
    
    def get_average_rating(self):
        ratings = self.fun_rating.all()
        values = [i.fun_rating for i in ratings]
        if ratings.exists():
            return sum(values) // ratings.count()
        return 0


class Category_hotel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории размещений"


class Hotel(models.Model):
    group = models.CharField(max_length=255, choices=[('food', 'ЕДА'), ('fun', 'РАЗВЛЕЧЕНИЯ'), ('hotel', 'РАЗМЕЩЕНИЕ')])
    category = models.ForeignKey(Category_hotel, related_name="category_hotel", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    info = models.TextField()
    address = models.CharField(max_length=255)
    hours = models.TextField(blank=True)
    image = models.ImageField(upload_to='hotel', blank=True)
    map_link = models.CharField(max_length=255, blank=True)
    hotel_link = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    
    class Meta:
        verbose_name = "Размещение"
        verbose_name_plural = "Размещение"
    
    def get_average_rating(self):
        ratings = self.hotel_rating.all()
        values = [i.hotel_rating for i in ratings]
        if ratings.exists():
            return sum(values) // ratings.count()
        return 0