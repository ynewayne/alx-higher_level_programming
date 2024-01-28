#!/bin/bash
# This script sends a GET request to a URL using curl and displays the body of the response
curl -sI "$1" | grep -i "HTTP/1.1 200 OK" && curl -s "$1"
