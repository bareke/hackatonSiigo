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


if __name__ == '__main__':
    generate_fake_data()
