# Generated by Django 4.2.11 on 2024-04-03 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_orderitems_user_cart_alter_payment_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='user_cart',
        ),
    ]
