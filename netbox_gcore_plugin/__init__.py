"""Netbox Plugin Configuration"""

from netbox.plugins import PluginConfig

class NetBoxGcoreConfig(PluginConfig):
    """Plugin Config Class"""

    name = "netbox_gcore_plugin"
    verbose_name = " NetBox GCore Plugin"
    description = "Manage GCore"
    version = "0.1.0"
    base_url = "gcore"
    min_version = "4.0.0"
    author= "Vincent Simonin <vincent@saashup.com>"
    author_email= "vincent@saashup.com"
    default_settings = {
        'gcore_base_url': 'https://api.gcore.com',
    }

    def ready(self):
        from . import signals # pylint: disable=unused-import, import-outside-toplevel

        return super().ready()


# pylint: disable=C0103
config = NetBoxGcoreConfig
