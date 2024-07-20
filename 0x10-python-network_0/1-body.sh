#!/bin/bash
# this script takes in a URL, sends a GET request
curl -sX GET "$1" -L
