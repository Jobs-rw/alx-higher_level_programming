#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL and an email, sends a POST request to the passed
    URL
    """
    url = argv[1]
    r = requests.post(url, data={'email': argv[2]})
    print(r.text)
