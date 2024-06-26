"""Gcore Plugin Models definitions"""

from django.db import models
from django.urls import reverse
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)
from taggit.managers import TaggableManager
from netbox.models import NetBoxModel

class ZoneAccount(NetBoxModel):
    """GCore account definition class"""

    token = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(limit_value=1),
            MaxLengthValidator(limit_value=255),
        ],
    )

    tags = TaggableManager(
        through="extras.TaggedItem", related_name="netbox_gcore_plugin_zoneaccount_set"
    )

    class Meta:
        """GCore zone account Model Meta Class"""

        ordering = ("token",)

    def __str__(self):
        return f"{self.token}"

    def get_absolute_url(self):
        """override"""
        return reverse("plugins:netbox_gcore_plugin:zoneaccount", args=[self.pk])


class ZoneZones(NetBoxModel):
    """GCore DNS zone definition class"""

    account = models.ForeignKey(
        ZoneAccount, on_delete=models.CASCADE, related_name="zones"
    )

    zone_name = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(limit_value=1),
            MaxLengthValidator(limit_value=255),
        ],
    )

    tags = TaggableManager(
        through="extras.TaggedItem", related_name="netbox_gcore_plugin_zonezones_set"
    )

    class Meta:
        """GCore DNS zone Model Meta Class"""

        ordering = ("zone_name",)

    def __str__(self):
        return f"{self.zone_name}"

    def get_absolute_url(self):
        """override"""
        return reverse("plugins:netbox_gcore_plugin:zonezones", args=[self.pk])


class DnsRecord(NetBoxModel):
    """DNS entry definition class"""

    CNAME = "CNAME"
    A = "A"

    TYPE_CHOICE = (
        (A, A),
        (CNAME, CNAME),
    )

    zone = models.ForeignKey(
        ZoneZones, on_delete=models.CASCADE, related_name="records"
    )
    record_id = name = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(limit_value=1),
            MaxLengthValidator(limit_value=32),
        ],
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(limit_value=1),
            MaxLengthValidator(limit_value=255),
        ],
    )
    type = models.CharField(
        max_length=64,
        choices=TYPE_CHOICE,
        default=CNAME,
        null=False,
        blank=False,
    )
    content = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(limit_value=1),
            MaxLengthValidator(limit_value=255),
        ],
    )
    ttl = models.IntegerField(
        default=3600,
        null=False,
        blank=False,
        validators=[
            MinValueValidator(limit_value=60),
            MaxValueValidator(limit_value=86400),
        ],
    )
    proxied = models.BooleanField(default=False, null=False, blank=False)
    tags = TaggableManager(
        through="extras.TaggedItem", related_name="netbox_gcore_plugin_dnsrecord_set"
    )

    class Meta:
        """DNS entry Meta Class"""

        ordering = (
            "zone",
            "name",
            "type",
        )
        constraints = (
            models.UniqueConstraint(
                fields=["zone", "name"],
                name="%(app_label)s_%(class)s_unique_zone_name_type_content",
            ),
        )

    def __str__(self):
        return f"{self.name} {self.type} {self.content} {self.ttl}"

    def get_absolute_url(self):
        """override"""
        return reverse("plugins:netbox_gcore_plugin:dnsrecord", args=[self.pk])
