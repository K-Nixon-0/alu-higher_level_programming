#!/bin/bash
# displays the body of a GET response, only if status code is 200
curl -s -o /tmp/body_$$ -w "%{http_code}" "$1" > /tmp/code_$$
code=$(cat /tmp/code_$$)
if [ "$code" -eq 200 ]; then
    cat /tmp/body_$$
fi
rm -f /tmp/body_$$ /tmp/code_$$
