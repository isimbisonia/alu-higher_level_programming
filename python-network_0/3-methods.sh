#!/bin/bash
# Displays all the HTTP methods the server will accept for the URL
curl -sI -X OPTIONS "$1" | grep -i "^Allow:" | cut -d " " -f2- | tr -d '\r'
