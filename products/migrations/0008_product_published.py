# Generated by Django 2.1.2 on 2018-10-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
