from django.urls import path
from django.urls import include
from rest_framework import routers

from .views import AcInvoiceItemsView
from .views import AcInvoicesView
from .views import AcProductsView
from .views import AcTenantView
from .views import CustomerView
from .views import DeviceView
from .views import SearchView
from .views import FakeData
from .views import FakeDataProducts

router = routers.DefaultRouter()
router.register('ac-invoice-items', AcInvoiceItemsView)
router.register('ac-invoices', AcInvoicesView)
router.register('ac-products', AcProductsView)
router.register('ac-tenant', AcTenantView)
router.register('customer', CustomerView)

router.register('device', DeviceView)
router.register('search', SearchView)


urlpatterns = [
    path('', include(router.urls)),
    path('fake/', FakeData.as_view(), name='fake_view'),
    path('fake-products/', FakeDataProducts.as_view(), name='fake_products_view'),
]
