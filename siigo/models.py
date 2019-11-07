from django.db import models

# Create your models here.


class Customer(models.Model):
    class Meta:
        db_table = 'customer'

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)


class AcInvoices(models.Model):
    class Meta:
        db_table = 'ac_invoices'

    ac_invoice_item = models.ForeignKey('AcInvoiceItems', on_delete=models.CASCADE)
    tenant = models.ForeignKey('AcTenant', on_delete=models.CASCADE)
    doc_date = models.CharField(max_length=45)
    doc_number = models.CharField(max_length=45)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    total_discount = models.IntegerField()
    total_tax = models.IntegerField()
    total_value = models.IntegerField()


class AcTenant(models.Model):
    class Meta:
        db_table = 'ac_tenant'

    name = models.CharField(max_length=45)


class AcInvoiceItems(models.Model):
    class Meta:
        db_table = 'ac_invoice_items'

    product = models.ForeignKey('AcProducts', on_delete=models.CASCADE)
    tenant = models.ForeignKey('AcTenant', on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit_value = models.FloatField()
    item_value = models.FloatField()


class AcProducts(models.Model):
    class Meta:
        db_table = 'ac_products'

    tenant = models.ForeignKey('AcTenant', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    description = models.TextField()
    list_price = models.FloatField()
