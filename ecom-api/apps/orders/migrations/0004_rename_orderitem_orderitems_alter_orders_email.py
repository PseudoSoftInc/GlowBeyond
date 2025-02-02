# Generated by Django 4.1.2 on 2022-12-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_price'),
        ('orders', '0003_alter_orderitem_quantity_alter_orders_phone_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='OrderItems',
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email address'),
        ),
    ]
