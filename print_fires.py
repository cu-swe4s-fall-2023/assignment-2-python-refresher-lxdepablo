import my_utils

country='United States of America'
country_column = 0
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
fires = my_utils.get_column(file_name, country_column, country, result_column = fires_column)
print(fires)
