def get_column(file_name, query_column, query_value, *, result_column = 1):
    # make an empty list to store results
    result_values = []

    # open the file and process it line by line
    with open(file_name, 'r') as file:
        for line in file:
            # split the line into an array using a comma as the delimiter
            parts = line.strip().split(',')

            # check if the value at the current position in query_column matches the query_value
            if parts[query_column] == query_value:
                # add the value in the result_column position to the result_values list
                result_values.append(parts[result_column])

    # Return the list of result values
    return result_values
