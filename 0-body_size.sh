#!/bin/bash
# It gets the size of the HTTP response header of a URL.
curl -s "$1" | wc -c
