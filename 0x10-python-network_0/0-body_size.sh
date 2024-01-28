#!/bin/bash
# This script takes a URL, sends a request using curl, and displays the size of the response body in bytes
# The URL is provided as a command-line argument

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

