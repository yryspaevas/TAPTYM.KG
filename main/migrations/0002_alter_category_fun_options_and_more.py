
# Generated by Django 4.1.5 on 2023-01-17 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category_fun',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории развлечений'},
        ),
        migrations.AlterModelOptions(
            name='category_hotel',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории размещений'},
        ),
        migrations.AlterModelOptions(
            name='category_place',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории заведений'},
        ),

        migrations.AlterModelOptions(
            name='fun',
            options={'verbose_name': 'Развлечение', 'verbose_name_plural': 'Развлечения'},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name': 'Размещение', 'verbose_name_plural': 'Размещение'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Еда', 'verbose_name_plural': 'Еда'},
        ),

    ]
