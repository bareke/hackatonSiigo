from rest_framework import serializers

from siigo.models import AcInvoiceItems
from siigo.models import AcInvoices
from siigo.models import AcProducts
from siigo.models import AcTenant
from siigo.models import Customer

from predictive.models import Device
from predictive.models import Search


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'


class AcInvoiceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcInvoiceItems
        fields = '__all__'


class AcInvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcInvoices
        fields = '__all__'


class AcProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcProducts
        fields = '__all__'


class AcTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcTenant
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
