from time import time
import random
from mixer.backend.django import mixer

from .models import AcInvoiceItems
from .models import AcInvoices
from .models import AcProducts
from .models import AcTenant
from .models import Customer

# Create your tests here.


def generate_fake_data(number):
    models = [AcInvoiceItems, AcInvoices, AcProducts, AcTenant, Customer]

    for model in models:
        mixer.cycle(number).blend(model)


def generate_fake_data_products(number):
    tenant = AcTenant.objects.first()
    items = AcInvoiceItems.objects.first()

    mixer.cycle(number).blend(
        AcProducts,
        tenant=tenant,
        ac_invoice_items=items
    )


def populate_products(records):
    list_name = ['zapato', 'cartera', 'chaqueta']
    description = 'lorem ipsum'
    list_price = [78.000, 125.000, 250.000]
    size = len(list_name) - 1

    tenant = AcTenant.objects.create(name='cueros colombia')

    print('-------------------------------------------')
    print('Generating {} de records...'.format(records))
    print('-------------------------------------------')
    instances = [
        AcProducts(
            name=list_name[random.randint(0, size)],
            description=description,
            list_price=list_price[random.randint(0, size)],
            tenant_id=tenant.id
        )
        for i in range(records)
    ]
    start_time = time()
    AcProducts.objects.bulk_create(instances)
    end_time = time()

    print('-------------------------------------------')
    print('Operation Time: {} seconds'.format(end_time - start_time))
    print('-------------------------------------------')


if __name__ == '__main__':
    generate_fake_data()
