# Generated by Django 4.2.7 on 2024-09-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_sale_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('sedan', 'Седан'), ('hatchback', 'Хэтчбек'), ('SUV', 'Внедорожник'), ('wagon', 'Универсал'), ('minivan', 'Минивэн'), ('pickup', 'Пикап'), ('coupe', 'Купе'), ('cabrio', 'Кабриолет')], max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='drive_unit',
            field=models.CharField(choices=[('rear', 'Задний'), ('front', 'Передний'), ('full', 'Полный')], max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('gasoline', 'Бензин'), ('diesel', 'Дизель'), ('hybrid', 'Гибрид'), ('electro', 'Электро')], max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='gearbox',
            field=models.CharField(choices=[('manual', 'Механика'), ('automatic', 'Автомат'), ('вариатор', 'CVT'), ('robot', 'Робот')], max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
