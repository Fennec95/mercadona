# Generated by Django 4.2.1 on 2023-05-18 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promotion',
            old_name='end_date',
            new_name='expiration_date',
        ),
    ]
