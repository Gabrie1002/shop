# Generated by Django 2.2 on 2022-06-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_product_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.TextField(blank=True, max_length=5, null=True, verbose_name='size'),
        ),
    ]
