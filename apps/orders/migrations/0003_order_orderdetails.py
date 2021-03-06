# Generated by Django 2.2 on 2022-06-03 04:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
        ('catalog', '0013_product_text'),
        ('orders', '0002_auto_20220603_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='datetime')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_orders', to='profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, verbose_name='count')),
                ('price', models.FloatField(default=0, verbose_name='price')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color_order_details', to='catalog.Color')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order_details', to='catalog.Product')),
            ],
        ),
    ]
