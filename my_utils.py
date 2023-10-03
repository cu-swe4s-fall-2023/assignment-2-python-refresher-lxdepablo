import sys


def get_column(file_name, query_column, query_value, *, result_column=1):

    """
    Retrieve values from a specified column in a CSV file based on a query.

    Parameters:
    - file_name (str): A path to a CSV file to read in.
    - query_column (int): Index of the column in the CSV to query.
    - query_value (str): The value to match in query_column.
    - result_column (int, optional): Index of the column to retrieve values
        from. Defaults to the second column (index 1).

    Returns:
    - list: A list of values from the specified result_column that match the
        query.

    """

    # make an empty list to store results
    result_values = []

    # open the file and process it line by line
    with open(file_name, 'r') as file:
        for line in file:
            # split the line into an array using a comma as the delimiter
            parts = line.strip().split(',')

            try:
                # check if the value at the current position in query_column
                # matches the query_value
                if parts[query_column] == query_value:
                    # cast value to integer
                    try:
                        # get result from result_column
                        result = parts[result_column]
                        # cast to float
                        result = float(result)
                        # cast to int
                        result = int(result)
                        # add the value in the result_column position to the
                        # result_values list
                        result_values.append(result)
                    except ValueError:
                        print("Value in result_column could not "
                              "be coerced to integer.")
                    except IndexError:
                        print("result_column index is out of bounds.")
                        sys.exit(1)
            except IndexError:
                print("query_column index is out of bounds.")
                sys.exit(1)

    # Return the list of result values
    return result_values


def mean(a):
    
    """
    Calculate the mean of a list of integers.

    Args:
    a (list of integers): The list of numbers for which the mean is to be calculated.

    Returns:
    float: The mean of the input list 'a'.
    """
    
    if len(a) == 0:
        return None
    num_sum = 0
    for number in a:
        try:
            num_sum += number
        except TypeError:
            print("Input must be a list of integers")
            return None
    output = num_sum/len(a)
    return(output)


def median(a):

    """
    Calculate the median of a list of integers.

    Args:
    a (list of integers): The list of numbers for which the median is to be calculated.

    Returns:
    float: The median of the input list 'a'.
    """

    # check if input is empty
    if len(a) == 0:
        return None
    # check if input has the right type
    for number in a:
        if type(number) != int:
            print("Input must be a list of integers")
            return None
    try:
        sorted_input = sorted(a)
    except TypeError:
        print("Input must be a list of integers")
        return None
    if len(sorted_input) % 2 == 0:
        hi_med_index = int(len(sorted_input)/2)
        low_med_index = hi_med_index-1
        output = mean([sorted_input[hi_med_index], sorted_input[low_med_index]])
    else:
        med_index = int(len(sorted_input)/2)
        output = sorted_input[med_index]
    return output


def standard_deviation(a):
    
    """
    Calculate the standard deviation of an array of integers.

    Args:
    a (list of integers): The list of integers for which the standard deviation is to be calculated.

    Returns:
    float: The standard deviation of the input array.
    """
    
    # check if input is long enough
    if len(arr) < 2:
        print("Standard deviation requires at least two data points")
        return None
    # check if input has the right type
    for number in a:
        if type(number) != int:
            print("Input must be a list of integers")
            return None

    # calculate the mean of the array
    mean = mean(a)

    # calculate the squared differences from the mean    
    squared_diffs = 0
    for x in a:
        squared_diffs += ((x-mean) ** 2)
    
    # divide by population size to get variance
    variance = squared_diffs/len(a)

    # standard deviation is the square root of the variance
    std_dev = variance ** 0.5

    return std_dev

