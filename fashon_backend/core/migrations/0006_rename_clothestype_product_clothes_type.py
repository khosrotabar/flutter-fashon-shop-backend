# Generated by Django 5.0.7 on 2024-08-05 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_isfeatured_product_is_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='clothesType',
            new_name='clothes_type',
        ),
    ]
