#!/bin/bash
# This script sends a GET request to a URL using curl, including a specific header, and displays the body of the response

curl -sH "X-School-User-Id: 98" "$1"
