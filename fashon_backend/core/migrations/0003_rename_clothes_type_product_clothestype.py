# Generated by Django 5.0.7 on 2024-08-05 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_rating_product_ratings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='clothes_type',
            new_name='clothesType',
        ),
    ]
