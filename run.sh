#!/bin/bash

# Check if the Python script exists
if [ -f "print_fires.py" ]; then
    # Run the Python script
    python print_fires.py
else
    echo "Error: The 'print_fires.py' script does not exist in the current directory."
    exit 1
fi