# Generated by Django 4.1.1 on 2023-01-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0017_stock_alter_customer_secret_for_2fa_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='stock_id',
            new_name='stock_uuid',
        ),
    ]
