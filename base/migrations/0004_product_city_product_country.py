# Generated by Django 4.1.2 on 2022-10-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
