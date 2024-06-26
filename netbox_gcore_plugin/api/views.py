"""API views definitions"""

from netbox.api.viewsets import NetBoxModelViewSet
from .serializers import ZoneAccountSerializer, DnsRecordSerializer, ZoneZonesSerializer
from ..models import ZoneAccount, DnsRecord, ZoneZones

class ZoneZonesViewSet(NetBoxModelViewSet):
    """ZoneZones view set class"""

    queryset = ZoneZones.objects.all()
    serializer_class = ZoneZonesSerializer
    http_method_names = ["get", "post", "delete", "options"]

class ZoneAccountViewSet(NetBoxModelViewSet):
    """ZoneAccount view set class"""

    queryset = ZoneAccount.objects.all()
    serializer_class = ZoneAccountSerializer
    http_method_names = ["get", "post", "delete", "options"]


class DnsRecordViewSet(NetBoxModelViewSet):
    """DnsRecord view set class"""

    queryset = DnsRecord.objects.all()
    serializer_class = DnsRecordSerializer
    http_method_names = ["get", "post", "delete", "options"]
