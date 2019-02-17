#!/bin/bash

trap "exit" INT TERM ERR
trap "kill 0" EXIT

# start resolver
FLASK_APP=app.py flask run --port=8300 &

# start cantaloupe
java -Dcantaloupe.config=cantaloupe.properties -Xmx2g -jar ./cantaloupe*/*.war 2>&1 | grep -v Font &


