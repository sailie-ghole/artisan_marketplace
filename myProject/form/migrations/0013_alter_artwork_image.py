# Generated by Django 4.2.4 on 2023-09-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0012_alter_artwork_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='form_images'),
        ),
    ]
