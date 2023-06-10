# Generated by Django 4.2.1 on 2023-06-08 11:51

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0011_alter_produkitem_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkitem',
            name='harga',
            field=models.DecimalField(decimal_places=3, default=Decimal('6.00'), max_digits=8),
        ),
        migrations.AlterField(
            model_name='produkitem',
            name='harga_diskon',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
    ]
