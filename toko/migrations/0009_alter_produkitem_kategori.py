# Generated by Django 4.2.1 on 2023-06-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0008_alter_alamatpengiriman_options_payment_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkitem',
            name='kategori',
            field=models.CharField(choices=[('D', 'Dress'), ('B', 'Blouse'), ('SW', 'Sweatshirt'), ('C', 'Celana'), ('Pl', 'Playsuit\xa0&\xa0Jumpsuit')], max_length=2),
        ),
    ]
