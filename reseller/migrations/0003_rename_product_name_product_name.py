# Generated by Django 3.2.16 on 2022-12-17 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reseller', '0002_alter_product_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]
