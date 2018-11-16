import sys
import json

a = '{"vnets": [{"domain_id": "3c12ccdf-9b8f-4d9b-8aa6-a523897e97a1", "acl_id": null, "arp_rate": null, "az_name": null, "id": "293c16a5-c757-405c-a693-3b2a3adead50", "bc_rate": null, "enable_ipv6": false, "arp_on": true, "tenant_id": "c7f3c2487eb34bbbbad16f76da2e2eb7", "project_id": "c7f3c2487eb34bbbbad16f76da2e2eb7", "type": "endpoint", "default_route_id": null, "updated_date": null, "subnets": [{"updated_date": null, "deleted": false, "ip": "10.0.0.0", "dhcp_ip_start": "10.0.0.1", "id": "92a9e440-0c90-41e7-9b1c-79a69de97e64", "name": null, "enable_dhcp": true, "mask": 24, "gateway_ip": "10.0.0.1", "vnet_id": "293c16a5-c757-405c-a693-3b2a3adead50", "created_date": "2016-04-20 16:30:55", "ip_version": 4, "dhcp_ip_end": "10.0.0.254"}], "tun_on": false, "deleted": false, "vni": 4919, "multicast_on": false, "broadcast_on": false, "name": "public-test-end", "enable_dhcp": true, "dns2": null, "dns1": null, "host_type": "", "dhcp_gw": null, "mode": "compact", "created_date": "2016-04-20 16:30:55", "natpool_id": null}]}'


def convert(data):
    data.replace("null", " ", -1)
    data_dict = json.loads(data)
    print json.dumps(data_dict, indent=4)


if __name__ == '__main__':

    convert(a)

