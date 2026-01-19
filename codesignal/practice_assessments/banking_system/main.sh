#!/bin/bash
echo "> python3 -m unittest discover -s tests -p '*.py' 2>&1"
python3 -m unittest discover -s tests -p '*.py' 2>&1
