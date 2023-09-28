#!/bin/bash
# takes in a URL, sends a request to that URL.
curl -sX GET $1 -L
