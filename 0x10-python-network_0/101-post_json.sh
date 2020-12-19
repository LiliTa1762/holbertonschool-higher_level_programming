#!/bin/bash
# sends a JSON POST
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
