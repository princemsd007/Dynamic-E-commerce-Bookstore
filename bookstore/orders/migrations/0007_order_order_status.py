# Generated by Django 4.2.5 on 2023-12-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0006_order_coupon_order_discount"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("processing", "Processing"),
                    ("shipped", "Shipped"),
                    ("canceled", "Canceled"),
                ],
                default="pending",
            ),
        ),
    ]
