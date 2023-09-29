#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print("Body response:")
            print("\t- type :", type(html))
            print("\t- content :", html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error: {} {}".format(e.code, e.reason))
