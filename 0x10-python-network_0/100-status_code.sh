#!/bin/bash
#code status
curl -o /dev/null --silent --head --write-out '%{http_code}\n' $1
