#!/bin/bash

trap "exit" INT TERM ERR
trap "kill 0" EXIT

# start resolver
gunicorn -w 4 -b 127.0.0.1:8300 app:app & java -Dcantaloupe.config=cantaloupe.properties -Xmx2g -jar ./cantaloupe*/*.war 2>&1 | grep -v Font 


