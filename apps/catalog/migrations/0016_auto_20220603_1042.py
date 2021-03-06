# Generated by Django 2.2 on 2022-06-03 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_remove_product_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5, verbose_name='size')),
                ('publish', models.BooleanField(default=True, verbose_name='publish')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(related_name='size_products', to='catalog.Size'),
        ),
    ]
