import urllib.error
import json
import sys
import urllib.request


def lookup_ip(ip_address):
    url = f"https://internetdb.shodan.io/{ip_address}"

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "CodePath-CYB101-Learning/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            data = json.load(response)
        return data

    except urllib.error.HTTPError as error:
        print("Shodan returned HTTP error:", error.code)
        return {}


if __name__ == "__main__":
    ip_address = sys.argv[1]
    result = lookup_ip(ip_address)

    if not result:
        print("No Shodan information available for this IP.")
        sys.exit(0)

    print("IP Address:", result.get("ip"))
    print("Hostnames:", result.get("hostnames", []))
    print("Open Ports:", result.get("ports", []))
    print("CVE Count:", len(result.get("vulns", [])))