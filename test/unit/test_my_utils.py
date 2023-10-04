import sys

sys.path.insert(0, '../../src')  # noqa

# import dependencies
import my_utils
import random
import unittest
import statistics
import csv


# make tester class
class TestMyUtils(unittest.TestCase):
    # function must be titled "test_asdf" to run as a test

    # setup/teardown functions
    def setUp(self):
        # Define the filename for the CSV file
        filename = "test_data.csv"

        # Open the CSV file for writing
        with open(filename, mode='w') as file:
            # Write the header row
            file.write("Query Column,Float Column 1,Float Column 2\n")

            # Generate and write 5 rows of data
            for i in range(5):
                string_value = f"country {i + 1}"

                # Generate random float values for the two float columns
                float_value1 = round(random.uniform(1.0, 10.0), 2)
                float_value2 = round(random.uniform(0.1, 1.0), 2)

                # Write the row to the CSV file
                file.write(f"{string_value},{float_value1},{float_value2}\n")
       
    def TearDown(self):
        os.remove("test_data.csv")
        
    # test mean, median, standard_deviation
    # positive cases
    def test_mean(self):
        arr = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
        m = my_utils.mean(arr)
        test_m = sum(arr)/3
        self.assertEqual(test_m, m)

    def test_median_odd(self):
        arr = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
        m = my_utils.median(arr)
        sorted_arr = sorted(arr)
        test_m = sorted_arr[1]
        self.assertEqual(test_m, m)

    def test_median_even(self):
        arr = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
        m = my_utils.median(arr)
        sorted_arr = sorted(arr)
        test_m = (sorted_arr[1] + sorted_arr[2])/2
        self.assertEqual(test_m, m)

    def test_stddev(self):
        arr = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
        sd = round(my_utils.standard_deviation(arr),3)
        test_sd = round(statistics.stdev(arr),3)
        self.assertEqual(test_sd, sd)

    # negative cases
    def test_mean_input_empty(self):
        arr = []
        m = my_utils.mean(arr)
        self.assertEqual(None, m)

    def test_mean_wrong_type(self):
        arr = ["1", "2", "3"]
        m = my_utils.mean(arr)
        self.assertEqual(None, m)

    def test_median_wrong_type(self):
        arr = ["1", "2", "3"]
        m = my_utils.median(arr)
        self.assertEqual(None, m)

    def test_stddev_input_too_small(self):
        arr = [random.randint(1,100)]
        sd = my_utils.standard_deviation(arr)
        self.assertEqual(None, sd)
        
    # test get_columns
    # positive case
    def test_get_cols(self):
        data = my_utils.get_column("test_data.csv", 0, "country 1", result_column=1)
        
        query_value = "country 1"
        # initialize a list to store matching values from Column 1
        matching_values = []

        # open and read the CSV file
        with open('test_data.csv', mode='r', newline='') as file:
            csv_reader = csv.reader(file)

            # Iterate through each row in the CSV
            for row in csv_reader:
                if len(row) >= 2 and row[0] == query_value:
                    # If the value in Column 0 matches the query, add the value from Column 1 to the list
                    matching_values.append(int(float(row[1])))
        
        self.assertEqual(matching_values, data)
    
    def test_get_cols_out_of_bounds(self):
        data = my_utils.get_column("test_data.csv", 0, "country 1", result_column=100)
        self.assertEqual(None, data)
        

if __name__ == '__main__':
    unittest.main()
