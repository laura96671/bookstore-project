# Generated by Django 4.0.4 on 2022-06-14 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
