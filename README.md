[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

my_utils contains a function called get_columns, which takes as input a csv file, the index of a column to query, a value to look for in that column, and optionally as a keyword argument the index of a column to return from as the result.

print_fires.py uses get_columns to print all the forest fires that happened in the USA from a CSV file containing various data. print_fires takes arguments for get_columns from the command line.
usage:
python print_fires.py -a [COUNTRY NAME] -b [QUERY COLUMN] -c [RESULT COLUMN] -d [FILEPATH]

run.sh runs print_fires.py.

Presentation:
I was interested in the relationship between increasing temperatures and CO2 emissions from forest fires. I thought that as temperatures increased, the frequency of forest fires and their associated CO2 emissions would also increase. However, although average temperature has a positive relationship with the year, there is no relationship between CO2 emissions due to forest fires and either year or temperature.