#!/bin/bash
# this script takes a URL, sends a request
curl -s "$1" | wc -c
