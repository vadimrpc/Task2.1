# Generated by Django 4.2.7 on 2024-09-25 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_sale_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.client'),
        ),
    ]
