# Generated by Django 5.0 on 2023-12-20 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=60, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='brand/logo')),
                ('banner', models.ImageField(blank=None, null=True, upload_to='brand/banner')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=60, unique=True)),
                ('description', models.TextField()),
                ('oprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/image')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='brand', to='shop.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='shop.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='seller', to='shop.seller')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/image')),
                ('review', models.TextField()),
                ('rating', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='shop.product')),
            ],
        ),
    ]
