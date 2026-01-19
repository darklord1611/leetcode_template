#!/bin/sh
python3 -m unittest discover -s tests  -p "*.py" -k "$1" 2>&1