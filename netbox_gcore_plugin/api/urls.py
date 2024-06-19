"""API URLs definition"""

from netbox.api.routers import NetBoxRouter
from .views import ZoneAccountViewSet, DnsRecordViewSet


APP_NAME = "netbox_gcore_plugin"

router = NetBoxRouter()
router.register("dns/accounts", ZoneAccountViewSet)
router.register("dns/records", DnsRecordViewSet)

urlpatterns = router.urls
