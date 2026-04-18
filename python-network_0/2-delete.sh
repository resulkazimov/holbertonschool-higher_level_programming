#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body
curl -sX DELETE "$1"
