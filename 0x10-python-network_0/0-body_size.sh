#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command-line argument
url="$1"

# Use curl to send a request and store the response in a variable
response=$(curl -sI "$url")

# Extract the Content-Length header from the response
content_length=$(echo "$response" | grep -iE '^Content-Length:' | awk '{print $2}')

# Check if Content-Length is present in the response
if [ -z "$content_length" ]; then
  echo "Content-Length header not found in the response."
  exit 1
fi

# Display the size in bytes
echo "Size of the response body: $content_length bytes"
