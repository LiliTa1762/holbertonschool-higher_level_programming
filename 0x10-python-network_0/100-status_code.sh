#!/bin/bash
#code status
curl -so /dev/null "$1" -w '%{http_code}\n'
