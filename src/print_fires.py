import my_utils
import argparse
import sys

# create an argument parser object
parser = argparse.ArgumentParser(
    description="Takes args for get_column from cmd line")

# define arguments to take from the command line
parser.add_argument("-a",
                    "--country",
                    type=str,
                    help="Name of the country (string)")
parser.add_argument("-b",
                    "--country_column",
                    type=int,
                    help="Column that your country's data is in (int)")
parser.add_argument("-c",
                    "--fires_column",
                    type=int,
                    help="Column to retrieve data from (int)")
parser.add_argument("-d",
                    "--file_name",
                    type=str,
                    help="Name of your file to read in (string)")
parser.add_argument("-e",
                    "--summary_fun",
                    type=str,
                    default=None,
                    help="Name of stats function to pass return data to."
                    "Can be mean, median, or standard_deviation")

# get commmand line input
args = parser.parse_args()

# store arguments in variables
country = args.country
country_column = args.country_column
fires_column = args.fires_column
file_name = args.file_name

# read in fire data from csv file
try:
    fires = my_utils.get_column(file_name,
                                country_column,
                                country,
                                result_column=fires_column)
except TypeError:
    print("Arguments of correct type must be supplied.")
except FileNotFoundError:
    print("No file was found at path ", file_name, ".")
    sys.exit(1)

# if a summary function was provided, run it on data
if args.summary_fun != None:
    summary_fun = args.summary_fun
    if summary_fun == "mean":
        fires_sum = my_utils.mean(fires)
    elif summary_fun == "median":
        fires_sum = my_utils.median(fires)
    elif summary_fun == "standard_deviation":
        fires_sum = my_utils.standard_deviation(fires)
    else:
        print("Summary function must be either 'mean',"
        "'median', or 'standard_deviation")
        sys.exit(1)

def main():
    if args.summary_fun != None:
        print(fires_sum)
    else:
        print(fires)


if __name__ == '__main__':
    main()
