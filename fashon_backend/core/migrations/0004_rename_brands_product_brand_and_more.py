# Generated by Django 5.0.7 on 2024-08-05 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_clothes_type_product_clothestype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='brands',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='create_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='imageUrls',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='is_featured',
            new_name='isFeatured',
        ),
    ]
