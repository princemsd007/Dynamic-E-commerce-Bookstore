# Generated by Django 4.2.5 on 2023-10-31 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_remove_order_apartment_remove_order_city_and_more"),
        ("user", "0005_shippingaddress_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shippingaddress",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shipping_addresses",
                to="orders.order",
            ),
        ),
    ]
