# Generated by Django 4.2.4 on 2023-09-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0019_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
