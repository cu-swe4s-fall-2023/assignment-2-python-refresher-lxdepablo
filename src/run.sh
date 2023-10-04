#!/bin/bash

# Check if the Python script exists
if [ -f "print_fires.py" ]; then
    # Run the python script
    python print_fires.py -a Samoa -b 0 -c 3 -d "../data/Agrofood_co2_emission.csv" -e standard_deviation
    # Run the python script, but throw errors
    python print_fires.py -a Samoa -b 0 -c 500 -d "../data/Agrofood_co2_emission.csv"
    python print_fires.py -a Samoa -b 0 -c 3 -d "doesnt_exist.csv"
else
    echo "Error: The 'print_fires.py' script does not exist in the current directory."
    exit 1
fi