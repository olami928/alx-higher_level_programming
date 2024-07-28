#!/bin/bash
# this script takes a URL ans=d send a GET request to the URL
curl -sX GET "$1" -H "X-School-User-Id: 98" -L
