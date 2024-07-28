#!/bin/bash
# this script takes in a URL and sends a POST request to it
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD" -L
