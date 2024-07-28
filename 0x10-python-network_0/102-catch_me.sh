#!/bin/bash
# this is a bash script thatmakes a request to 0.0.0.0:5000/catch_me
curl -s -X POST -H "Content-Type: application/json" -d \\
'{"user_id":"98"}' http://0.0.0.0:5000/catch_me
