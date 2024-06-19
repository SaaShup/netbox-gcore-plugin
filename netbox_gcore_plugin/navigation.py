"""Navigation Menu definitions"""

from netbox.plugins import (
    PluginMenu,
    PluginMenuItem,
    PluginMenuButton,
)

zoneaccount_buttons = [
    PluginMenuButton(
        link="plugins:netbox_gcore_plugin:zoneaccount_add",
        title="Add",
        icon_class="mdi mdi-plus-thick"
    )
]

dnsrecord_buttons = [
    PluginMenuButton(
        link="plugins:netbox_gcore_plugin:dnsrecord_add",
        title="Add",
        icon_class="mdi mdi-plus-thick"
    )
]

account_item = [
    PluginMenuItem(
        link="plugins:netbox_gcore_plugin:zoneaccount_list",
        link_text="Accounts",
        buttons=zoneaccount_buttons,
        permissions=["netbox_gcore_plugin.view_zoneaccount"],
    )
]

dns_item = [
    PluginMenuItem(
        link="plugins:netbox_gcore_plugin:dnsrecord_list",
        link_text="Records",
        buttons=dnsrecord_buttons,
        permissions=["netbox_gcore_plugin.view_dnsrecord"],
    ),
]

menu = PluginMenu(
    label="Gcore",
    groups=(("ACCOUNTS", account_item),("DNS ZONE", dns_item),),
    icon_class="mdi mdi-cloud",
)
