# Generated by Django 4.2.11 on 2024-04-03 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_remove_orderitems_user_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_id',
        ),
    ]