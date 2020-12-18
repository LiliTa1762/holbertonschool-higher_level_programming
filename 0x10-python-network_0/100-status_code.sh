#!/bin/bash
#code status
curl -so /dev/null --silent --head --write-out '%{http_code}\n' $1
