#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_print_fires python print_fires.py -a Samoa -b 0 -c 3 -d "../data/Agrofood_co2_emission.csv" -e mean
assert_in_stdout 0.5161290322580645
assert_exit_code 0