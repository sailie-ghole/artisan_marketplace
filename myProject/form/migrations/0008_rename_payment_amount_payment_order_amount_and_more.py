# Generated by Django 4.2.4 on 2023-09-04 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_rename_order_amount_payment_payment_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_amount',
            new_name='order_amount',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='payment_date',
            new_name='order_date',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='payment_id',
            new_name='order_payment_id',
        ),
    ]
