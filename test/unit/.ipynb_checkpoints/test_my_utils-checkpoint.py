import sys

sys.path.insert(0, '../../src')  # noqa

# import dependencies
import my_utils
import random
import unittest


# make tester class
class TestMyUtils(unittest.TestCase):
    # function must be titled "test_asdf" to run as a test

    # setup/teardown functions
    def SetUp(self):
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
    def test_mean_2(self):
        arr = [1, 2, 3]
        m = my_utils.mean(arr)
        self.assertEqual(2, m)

    def test_median_2_even(self):
        arr = [1, 2, 3, 10]
        m = my_utils.median(arr)
        self.assertEqual(2.5, m)

    def test_median_2_odd(self):
        arr = [1, 1, 2, 3, 10]
        m = my_utils.median(arr)
        self.assertEqual(2, m)

    def test_median_2_unsorted(self):
        arr = [2, 1, 10, 3, 1]
        m = my_utils.median(arr)
        self.assertEqual(2, m)

    def test_stddev_1(self):
        arr = [1, 2, 3]
        m = my_utils.standard_deviation(arr)
        self.assertEqual(0.816496580927726, m)

    def test_stddev_1_negative(self):
        arr = [-1, -2, -3]
        m = my_utils.standard_deviation(arr)
        self.assertEqual(0.816496580927726, m)

    # edge cases
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
        arr = [1]
        m = my_utils.standard_deviation(arr)
        self.assertEqual(None, m)

    # negative cases
    def test_mean_not_3(self):
        arr = [1, 2, 3]
        m = my_utils.mean(arr)
        self.assertNotEqual(3, m)

    def test_median_not_3(self):
        arr = [1, 2, 3]
        m = my_utils.median(arr)
        self.assertNotEqual(3, m)

    def test_stddev_not_3(self):
        arr = [1, 2, 3]
        m = my_utils.standard_deviation(arr)
        self.assertNotEqual(3, m)


if __name__ == '__main__':
    unittest.main()
