# Generated by Django 4.0.4 on 2022-06-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]