# Generated by Django 2.2.7 on 2019-11-07 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcInvoiceItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('unit_value', models.FloatField()),
                ('item_value', models.FloatField()),
            ],
            options={
                'db_table': 'ac_invoice_items',
            },
        ),
        migrations.CreateModel(
            name='AcTenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'ac_tenant',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='AcProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('list_price', models.FloatField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siigo.AcTenant')),
            ],
            options={
                'db_table': 'ac_products',
            },
        ),
        migrations.CreateModel(
            name='AcInvoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_date', models.CharField(max_length=45)),
                ('doc_number', models.CharField(max_length=45)),
                ('total_discount', models.IntegerField()),
                ('total_tax', models.IntegerField()),
                ('total_value', models.IntegerField()),
                ('ac_invoice_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siigo.AcInvoiceItems')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siigo.Customer')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siigo.AcTenant')),
            ],
            options={
                'db_table': 'ac_invoices',
            },
        ),
        migrations.AddField(
            model_name='acinvoiceitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siigo.AcProducts'),
        ),
        migrations.AddField(
            model_name='acinvoiceitems',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siigo.AcTenant'),
        ),
    ]
