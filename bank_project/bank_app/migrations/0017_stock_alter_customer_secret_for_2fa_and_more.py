# Generated by Django 4.1.1 on 2023-01-13 11:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0016_merge_20230107_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.UUIDField()),
                ('stock_company_name', models.CharField(max_length=30)),
                ('stock_symbol', models.CharField(choices=[('NOVOb', 'Novob'), ('GN', 'Gn'), ('DANSKE', 'Danske'), ('GMAB', 'Gmab'), ('DSV', 'Dsv'), ('MAERSKb', 'Maerskb'), ('VWS', 'Vws'), ('ORSTED', 'Orsted'), ('NZYMb', 'Nzymb'), ('AMBUb', 'Ambub'), ('CHRH', 'Chrh'), ('CARLb', 'Carlb'), ('PNDORA', 'Pndora'), ('JYSK', 'Jysk'), ('NDADK', 'Ndadk'), ('SYDB', 'Sydb')], max_length=8)),
                ('price_currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='secret_for_2fa',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='n_times_logged_in_with_email_auth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='externaltransfer',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='externaltransfer',
            name='idempotency_key',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Stocks_Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField()),
                ('stock_volume', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Minimum value is 1')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank_app.stock')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='belongs_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.customer'),
        ),
    ]
