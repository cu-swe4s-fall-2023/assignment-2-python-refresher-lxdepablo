#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_mean python ../../src/print_fires.py -a Samoa -b 0 -c 3 -d "../../data/Agrofood_co2_emission.csv" -e mean
assert_in_stdout 0.7154903225806452
assert_exit_code 0

run test_median python ../../src/print_fires.py -a Samoa -b 0 -c 3 -d "../../data/Agrofood_co2_emission.csv" -e median
assert_in_stdout 0
assert_exit_code 0

run test_stddev python ../../src/print_fires.py -a Samoa -b 0 -c 3 -d "../../data/Agrofood_co2_emission.csv" -e standard_deviation
assert_in_stdout 1.4190505098726727
assert_exit_code 0

run test_plot_ff_year python ../../src/plot_forfires_year.py "../../data/Agrofood_co2_emission.csv" "../../data/forfires_year.png" "Albania" "Albanian Forest Fires" "Year" "CO2 Emissions"
assert_equal $"../../data/forfires_year.png" $( ls $"../../data/forfires_year.png" )

run test_plot_ff_temp python ../../src/plot_forfires_temp.py "../../data/Agrofood_co2_emission.csv" "../../data/forfires_temp.png" "Albania" "Albanian Forest Fires" "Average Temperature" "CO2 Emissions"
assert_equal $"../../data/forfires_temp.png" $( ls $"../../data/forfires_temp.png" )

run test_plot_temp_year python ../../src/plot_temp_year.py "../../data/Agrofood_co2_emission.csv" "../../data/temp_year.png" "Albania" "Albanian Temperatures" "Year" "Average Temperature"
assert_equal $"../../data/temp_year.png" $( ls $"../../data/temp_year.png" )