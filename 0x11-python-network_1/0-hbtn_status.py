#!/usr/bin/python3

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type :", type(html))
        print("\t- content :", html.decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"Error: {e.code} {e.reason}")
except urllib.error.URLError as e:
    print(f"Error: {e.reason}")
