from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from siigo.models import AcInvoiceItems
from siigo.models import AcInvoices
from siigo.models import AcProducts
from siigo.models import AcTenant
from siigo.models import Customer
from .serializers import AcInvoiceItemsSerializer
from .serializers import AcInvoicesSerializer
from .serializers import AcProductsSerializer
from .serializers import AcTenantSerializer
from .serializers import CustomerSerializer

from predictive.models import Device
from predictive.models import Search
from .serializers import DeviceSerializer
from .serializers import SearchSerializer

from siigo.utils import generate_fake_data
from siigo.utils import populate_products


# Create your views here.


class DeviceView(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class SearchView(ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer


class AcInvoiceItemsView(ModelViewSet):
    queryset = AcInvoiceItems.objects.all()
    serializer_class = AcInvoiceItemsSerializer


class AcInvoicesView(ModelViewSet):
    queryset = AcInvoices.objects.all()
    serializer_class = AcInvoicesSerializer


class AcProductsView(ModelViewSet):
    queryset = AcProducts.objects.all()
    serializer_class = AcProductsSerializer


class AcTenantView(ModelViewSet):
    queryset = AcTenant.objects.all()
    serializer_class = AcTenantSerializer


class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class FakeData(APIView):
    def post(self, request):
        json = JSONParser().parse(request)
        number = int(json.get('number'))
        if number:
            generate_fake_data(number)
            content = {'successful data generation': 'fake data'}
            return JsonResponse(content, status=status.HTTP_200_OK)
        content = {'please send number': 'nothing to see here'}
        return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)


class FakeDataProducts(APIView):
    def post(self, request):
        json = JSONParser().parse(request)
        number = int(json.get('number'))
        if number:
            populate_products(number)
            content = {'successful data generation': 'fake data products'}
            return JsonResponse(content, status=status.HTTP_200_OK)
        content = {'please send number': 'nothing to see here'}
        return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)
