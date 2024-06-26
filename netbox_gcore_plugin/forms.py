"""Forms definitions"""

from django import forms
from utilities.forms.fields import (
    TagFilterField,
    DynamicModelMultipleChoiceField,
    DynamicModelChoiceField,
)
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import ZoneAccount, DnsRecord, ZoneZones

class ZoneZonesForm(NetBoxModelForm):
    """ZoneZones form definition class"""

    account = DynamicModelChoiceField(
        label="Account", queryset=ZoneAccount.objects.all(), required=True
    )

    class Meta:
        """ZoneZones form definition Meta class"""

        model = ZoneZones
        fields = (
            "account",
            "zone_name",
            "tags",
        )


class ZoneAccountForm(NetBoxModelForm):
    """ZoneAccount form definition class"""

    class Meta:
        """ZoneAccount form definition Meta class"""

        model = ZoneAccount
        fields = (
            "token",
            "tags",
        )


class DnsRecordForm(NetBoxModelForm):
    """DnsRecord form definition class"""

    zone = DynamicModelChoiceField(
        label="Zone", queryset=ZoneZones.objects.all(), required=True
    )

    class Meta:
        """DnsRecord form definition Meta class"""

        model = DnsRecord
        fields = (
            "zone",
            "name",
            "type",
            "content",
            "ttl",
            "proxied",
        )


class DnsRecordFilterForm(NetBoxModelFilterSetForm):
    """DnsRecord filter form definition class"""

    model = DnsRecord

    zone_name = DynamicModelMultipleChoiceField(
        queryset=ZoneZones.objects.all(),
        required=False,
        label="Zones",
    )
    type = forms.ChoiceField(
        label="Type", choices=DnsRecord.TYPE_CHOICE, required=False
    )
    tag = TagFilterField(model)
