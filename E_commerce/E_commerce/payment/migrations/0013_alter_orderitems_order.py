# Generated by Django 4.2.11 on 2024-04-03 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_order_order_total_gst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='Order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.order'),
        ),
    ]
