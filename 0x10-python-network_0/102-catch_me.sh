#!/usr/bin/bash
# this is a bash script thatmakes a request to 0.0.0.0:5000/catch_me
curl -sX -H "http://0.0.0.0:5000/catch_me" -d \\
'{"messamakes a request to 0.0.0.0:5000/catch_mege":"You got me!"}' "$1" -L
