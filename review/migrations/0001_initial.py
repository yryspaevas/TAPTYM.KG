# Generated by Django 4.1.5 on 2023-01-17 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_alter_category_place_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_rating', models.IntegerField(default=0)),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_rating', to='main.place')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_comments', to='main.place')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_rating', models.IntegerField(default=0)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_rating', to='main.hotel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_comments', to='main.hotel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FunRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fun_rating', models.IntegerField(default=0)),
                ('fun_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fun_rating', to='main.fun')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fun_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FunComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fun_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fun_comments', to='main.fun')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fun_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoritePlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_place', models.BooleanField(default=False)),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='main.place')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_hotel', models.BooleanField(default=False)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='main.hotel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteFun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_fun', models.BooleanField(default=False)),
                ('fun_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='main.fun')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fun_favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]