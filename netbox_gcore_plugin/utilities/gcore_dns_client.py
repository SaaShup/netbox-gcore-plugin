"""Gcore DNS Client"""

import requests
from ..models import DnsRecord


class GcoreDnsClient:
    """Gcore DNS Client"""

    zone_account = None
    base_url = None

    def __init__(self, zone_account, base_url):
        self.zone_account = zone_account
        self.base_url = base_url

    def get_dns_records(self, page=1, per_page=100):
        """Get DNS Record from Gcore"""

        url = f"{self.base_url}/dns/v2/zones/{self.zone_account.zone_name}"
        headers = {
            "Authorization": f"APIKey {self.zone_account.token}",
            "Content-Type": "application/json",
        }

        response = requests.get(
            url, headers=headers, timeout=5
        )

        response.raise_for_status()

        content = response.json()

       #result = {"result_info": content["rrsets_amount"]}
        result = {}

        result["records"] = []

        for record in content["records"]:
            if record["type"] in (DnsRecord.A, DnsRecord.CNAME):
                result["records"].append(
                    DnsRecord(
                        zone=self.zone_account,
                        record_id=0,
                        name=record["name"],
                        type=record["type"],
                        content=record["short_answers"][0],
                        ttl=record["ttl"],
                        proxied=False,
                    )
                )

        return result

    def create_dns_record(self, dns_record):
        """Add DNS Record to Gcore"""

        url = f"{self.base_url}/dns/v2/zones/{self.zone_account.zone_name}/{self.dns_record.name}/{dns_record.type}"
        headers = {
            "Authorization": f"APIKey {self.zone_account.token}",
            "Content-Type": "application/json",
        }

        response = requests.post(
            url,
            headers=headers,
            timeout=5,
            json={
                "resource_records": [{
                    "content": [dns_record.content]
                }],
                "ttl": dns_record.ttl,
            },
        )

        response.raise_for_status()

        content = response.json()

        dns_record.record_id = content["id"]

        return dns_record

    def delete_dnsrecord(self, dns_record):
        """Delete DNS Record to from"""

        url = f"{self.base_url}/dns/v2/zones/{self.zone_account.zone_id}/{self.dns_record.name}/{dns_record.type}"

        headers = {
            "Authorization": f"APIKey {self.zone_account.token}",
            "Content-Type": "application/json",
        }

        response = requests.delete(url, headers=headers, timeout=5)

        response.raise_for_status()
