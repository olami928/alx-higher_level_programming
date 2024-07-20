#!/usr/bin/bash
# this script takes a URL, sends a request
# to that URL, and displays the size of the body of the respons

curl -s "$1" | wc -c
