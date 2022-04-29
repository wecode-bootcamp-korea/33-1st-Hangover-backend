# Generated by Django 4.0.4 on 2022-04-28 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_alcohol_percentage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='average_rating',
        ),
    ]
