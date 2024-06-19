""" Hooks on Django model signals. """

from django.conf import settings
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from utilities.exceptions import AbortRequest
from .models import ZoneAccount, DnsRecord
from .utilities.gcore_dns_client import GcoreDnsClient


@receiver(post_save, sender=ZoneAccount)
def init_zoneaccount(instance, **_kwargs):
    """Init Zone Account by creating all dns record compatible"""

    if _kwargs.get("created") is True:
        client = GcoreDnsClient(
            instance,
            settings.PLUGINS_CONFIG["netbox_gcore_plugin"]["gcore_base_url"],
        )

        page = 1

        while True:
            result = client.get_dns_records(page=page)
            DnsRecord.objects.bulk_create(result["records"])

            if page == result["result_info"]["total_pages"]:
                break

            page = page + 1


@receiver(pre_save, sender=DnsRecord)
def create_dnsrecord(instance, **_kwargs):
    """Create a DNS Record on Gcore"""

    if instance.pk is None:
        client = GcoreDnsClient(
            instance.zone,
            settings.PLUGINS_CONFIG["netbox_gcore_plugin"]["gcore_base_url"],
        )

        try:
            instance = client.create_dns_record(instance)
        except Exception as e:
            raise AbortRequest("Unable to create DNS Record on Gcore") from e


@receiver(pre_delete, sender=DnsRecord)
def delete_dnsrecord(instance, **_kwargs):
    """Delte a DNS Record on Gcore"""

    if isinstance(_kwargs["origin"], DnsRecord):
        client = GcoreDnsClient(
            instance.zone,
            settings.PLUGINS_CONFIG["netbox_gcore_plugin"]["gcore_base_url"],
        )

        try:
            client.delete_dnsrecord(instance)
        except Exception as e:
            raise AbortRequest("Unable to delete DNS Record on Gcore") from e