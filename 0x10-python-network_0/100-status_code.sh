#!/bin/bash
# Sends a request to the URL passed as an argument and displays only the status code of the response

url=$1
curl -o /dev/null -s -w "%{http_code}" "$url"
