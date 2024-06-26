"""Tables definitions"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import ZoneAccount, DnsRecord, ZoneZones

class ZoneZonesTable(NetBoxTable):
    """ZoneZones Table definition class"""

    zone_name = tables.Column(linkify=True)
    dnsrecord_count = columns.LinkedCountColumn(
        viewname="plugins:netbox_gcore_plugin:dnsrecord_list",
        url_params={"zone_name": "pk"},
        verbose_name="Records count",
    )
    tags = columns.TagColumn()
    actions = columns.ActionsColumn(actions=("delete",))

    class Meta(NetBoxTable.Meta):
        """ZoneZones Table definition Meta class"""

        model = ZoneZones
        fields = (
            "pk",
            "id",
            "zone_name",
            "dnsrecord_count",
            "tags",
        )
        default_columns = ("zone_name", "dnsrecord_count")

class ZoneAccountTable(NetBoxTable):
    """ZoneAccount Table definition class"""

    token = tables.Column(linkify=True)
    zonezones_count = columns.LinkedCountColumn(
        viewname="plugins:netbox_gcore_plugin:zonezones_list",
        url_params={"account": "pk"},
        verbose_name="Zones count",
    )
    tags = columns.TagColumn()
    actions = columns.ActionsColumn(actions=("delete",))

    class Meta(NetBoxTable.Meta):
        """ZoneAccount Table definition Meta class"""

        model = ZoneAccount
        fields = (
            "pk",
            "id",
            "token",
            "zonezones_count",
            "tags",
        )
        default_columns = ("zone_name", "zonezones_count")


class DnsRecordTable(NetBoxTable):
    """DnsRecord Table definition class"""

    name = tables.Column(linkify=True)
    tags = columns.TagColumn()
    actions = columns.ActionsColumn(actions=("delete",))

    class Meta(NetBoxTable.Meta):
        """DnsRecord Table definition Meta class"""

        model = DnsRecord
        fields = (
            "pk",
            "id",
            "record_id",
            "name",
            "type",
            "content",
            "ttl",
            "proxied",
            "tags",
        )
        default_columns = ("name", "type", "content", "ttl", "proxied")
