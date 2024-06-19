"""API Serializer definitions"""

from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import ZoneAccount, DnsRecord


class NestedZoneAccountSerializer(WritableNestedSerializer):
    """Nested ZoneAccount Serializer class"""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_gcore_plugin-api:zoneaccount-detail"
    )

    class Meta:
        """Nested ZoneAccount Serializer Meta class"""

        model = ZoneAccount
        fields = (
            "id",
            "url",
            "display",
            "zone_name",
            "token",
        )


class NestedDnsRecordSerializer(WritableNestedSerializer):
    """Nested DnsRecord Serializer class"""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_gcore_plugin-api:dnsrecord-detail"
    )

    class Meta:
        """Nested DnsRecord Serializer Meta class"""

        model = DnsRecord
        fields = (
            "id",
            "url",
            "display",
            "record_id",
            "name",
            "type",
            "content",
            "ttl",
            "proxied",
        )


class DnsRecordSerializer(NetBoxModelSerializer):
    """DnsRecord Serializer class"""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_gcore_plugin-api:dnsrecord-detail"
    )

    class Meta:
        """DnsRecord Serializer Meta class"""

        model = DnsRecord
        fields = (
            "id",
            "url",
            "display",
            "record_id",
            "name",
            "type",
            "content",
            "ttl",
            "proxied",
            "custom_fields",
            "created",
            "last_updated",
            "tags",
        )
        brief_fields = NestedZoneAccountSerializer.Meta.fields


class ZoneAccountSerializer(NetBoxModelSerializer):
    """ZoneAccount Serializer class"""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_gcore_plugin-api:zoneaccount-detail"
    )

    class Meta:
        """ZoneAccount Serializer Meta class"""

        model = ZoneAccount
        fields = (
            "id",
            "url",
            "display",
            "zone_name",
            "token",
            "custom_fields",
            "created",
            "last_updated",
            "tags",
        )
        brief_fields = NestedZoneAccountSerializer.Meta.fields
