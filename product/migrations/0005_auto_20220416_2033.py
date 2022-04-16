# Generated by Django 3.2 on 2022-04-16 20:33

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_alter_property_listing_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('order_id', models.CharField(blank=True, default=None, max_length=50, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('img', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, default='Pending', max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Orderitem',
            },
        ),
        migrations.RemoveField(
            model_name='cartorderitems',
            name='order',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='useraddressbook',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='CartOrder',
        ),
        migrations.DeleteModel(
            name='CartOrderItems',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
        migrations.DeleteModel(
            name='ProductReview',
        ),
        migrations.DeleteModel(
            name='UserAddressBook',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='product.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
