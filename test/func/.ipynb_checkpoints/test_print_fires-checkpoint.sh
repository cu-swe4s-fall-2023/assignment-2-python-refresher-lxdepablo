#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_mean python ../../src/print_fires.py -a Samoa -b 0 -c 3 -d "../../data/Agrofood_co2_emission.csv" -e mean
assert_in_stdout 0.5161290322580645
assert_exit_code 0

run test_median python ../../src/print_fires.py -a Samoa -b 0 -c 3 -d "../../data/Agrofood_co2_emission.csv" -e median
assert_in_stdout 0
assert_exit_code 0

run test_stddev python ../../src/print_fires.py -a Samoa -b 0 -c 3 -d "../../data/Agrofood_co2_emission.csv" -e standard_deviation
assert_in_stdout 1.3384311149485302
assert_exit_code 0