# Generated by Django 4.1.1 on 2023-01-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0018_alter_externaltransfer_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
