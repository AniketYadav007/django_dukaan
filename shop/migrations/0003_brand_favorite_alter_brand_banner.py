# Generated by Django 5.0 on 2023-12-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_productimage_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='brand',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='brand/banner'),
        ),
    ]
