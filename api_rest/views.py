from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet

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

from siigo.utils import generate_fake_data
from siigo.utils import generate_fake_data_products

# Create your views here.


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
            return JsonResponse(json, status=status.HTTP_200_OK)
        content = {'please send number': 'nothing to see here'}
        return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)


class FakeDataProducts(APIView):
    def post(self, request):
        json = JSONParser().parse(request)
        number = int(json.get('number'))
        if number:
            generate_fake_data_products(number)
            return JsonResponse(json, status=status.HTTP_200_OK)
        content = {'please send number': 'nothing to see here'}
        return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)
