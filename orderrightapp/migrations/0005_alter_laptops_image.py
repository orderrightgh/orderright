# Generated by Django 5.1.6 on 2025-03-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderrightapp', '0004_laptops_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptops',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
