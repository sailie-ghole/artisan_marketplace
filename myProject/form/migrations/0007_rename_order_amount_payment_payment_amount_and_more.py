# Generated by Django 4.2.4 on 2023-09-04 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='order_amount',
            new_name='payment_amount',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='order_payment_id',
            new_name='payment_id',
        ),
    ]