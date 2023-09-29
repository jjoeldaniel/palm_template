#!/usr/bin/env bash

# Clean ./uploads
rm -rf ./uploads

# Determine Python base command
PY_BASE=""
if command -v python3 &> /dev/null
then
	PY_BASE="python3"
elif command -v python &> /dev/null
then
	PY_BASE="python"
fi

# Run or display error
if [ -z "$PY_BASE" ]
then
	echo "u dont have python :("
else
	echo "u have python :)"
	$PY_BASE app/main.py
fi
