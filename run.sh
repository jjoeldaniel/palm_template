#!/usr/bin/env bash

PY_BASE=""
if command -v python3 &> /dev/null
then
	PY_BASE="python3"
elif command -v python &> /dev/null
then
	PY_BASE="python"
fi

if [ -z "$PY_BASE" ]
then
	echo "u dont have python :("
else
	echo "u have python :)"
	$PY_BASE app/main.py
fi
