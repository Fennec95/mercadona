# Generated by Django 4.2.1 on 2023-05-19 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
